#!/usr/bin/python3
"""
creating session Authentication routes
"""
from flask import Flask
from flask import jsonify, abort, request, session
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User
from models import db_session


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    returns  status
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify(error="email missing"), 400
    if password is None:
        return jsonify(error="password missing"), 400
    user = db_session.query(User).filter_by(email=email).first()
    if user is None:
        return jsonify(error="no user found for this email"), 404
    if user.is_valid_password(password) is False:
        return jsonify(error="wrong password"), 401
    user_id = user.id
    sessionID = auth.create_session(user_id)
    d_user = user.to_dict()
    session[HBNB_YELP_SESSION_NAME] = HBNB_YELP_SESSION_NAME
    return jsonify(d_user)
