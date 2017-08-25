from flask import Flask
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from models import db_session

@app_views.route('/users', strict_slashes=False)
def users():
    users = User.all()
    user_array = []
    for user in users:
        user_array.append(user.to_dict())
    return jsonify(user_array)

@app_views.route('/users/<user_id>', strict_slashes=False)
def user(user_id):
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        d_user = user.to_dict()
        return jsonify(d_user)

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        db_session.commit()
        return jsonify()

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    if request.get_json():
        json = request.get_json()
        email = json.get('email')
        password = json.get('password')
        if email is None:
            return jsonify(error="email missing"), 400
        if password is None:
            return jsonify(error="password missing"), 400
        if json.get('first_name') is None and json.get('last_name') is None:
            newUser = User()
            newUser.email = json['email']
            newUser.password = json['password']
        else:
            newUser = User()
            newUser.email = json['email']
            newUser.password = json['password']
            newUser.first_name = json['first_name']
            newUser.last_name = json['last_name']
        db_session.add(newUser)
        db_session.commit()
        created_user = User.last().to_dict()
        return jsonify(created_user), 201
    else:
        return jsonify(error="Wrong format")
