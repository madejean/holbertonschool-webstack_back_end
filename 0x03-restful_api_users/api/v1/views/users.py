#!/usr/bin/python3
"""
creating user routes
"""
from flask import Flask
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from models import db_session


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """
    returns list of users
    """
    users = User.all()
    user_array = []
    for user in users:
        user_array.append(user.to_dict())
    return jsonify(user_array)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def user(user_id):
    """
    retrieves a specific user
    """
    if user_id == me and request.current_user is None:
        return abort(404)
    if user_id == me and request.current_user:
        return me
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        d_user = user.to_dict()
        return jsonify(d_user)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    retrieves an user and deletes it
    """
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        db_session.commit()
        return jsonify()


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    creates an user
    """
    if request.get_json():
        json = request.get_json()
        email = json.get('email')
        password = json.get('password')
        if email is None:
            return jsonify(error="email missing"), 400
        if password is None:
            return jsonify(error="password missing"), 400
        try:
            newUser = User()
            newUser.email = json['email']
            newUser.password = json['password']
        except:
            return jsonify(error="Can't create User: <exception message>"), 400
        if json.get('first_name'):
            newUser.first_name = json['first_name']
        if json.get('last_name'):
            newUser.last_name = json['last_name']

        db_session.add(newUser)
        db_session.commit()
        created_user = User.last().to_dict()
        return jsonify(created_user), 201

    else:
        return jsonify(error="Wrong format"), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    updates an user
    """
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    if request.get_json():
        json = request.get_json()
        if json.get('first_name'):
            user.first_name = json['first_name']
        if json.get('last_name'):
            user.last_name = json['last_name']
        db_session.commit()
        d_user = user.to_dict()
        return jsonify(d_user)
    else:
        return jsonify(error="Wrong format"), 400


@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def me():
    user = db_session.query(User).get(request.current_user.id)
    if user is None:
        return abort(404)
    d_user = user.to_dict()
    return jsonify(d_user)
