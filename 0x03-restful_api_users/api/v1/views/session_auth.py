#!/usr/bin/python3
"""
creating session Authentication routes
"""
from flask import Flask
from flask import jsonify, abort, request, session
import os
from api.v1.views import app_views
from models.user import User
from models import db_session


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    login route
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
    sessionID = auth.create_session(user.id)
    HBNB_YELP_SESSION_NAME = os.environ.get('HBNB_YELP_SESSION_NAME')
    d_user = user.to_dict()
    out = jsonify(d_user)
    out.set_cookie(HBNB_YELP_SESSION_NAME, sessionID)
    return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """
    logout route
    """
    clear_session = auth.destroy_session(request)
    if clear_session is False:
        return abort(404)
    else:
        return jsonify({}), 200
