#!/usr/bin/python3
"""
creating session Authentication routes
"""
from flask import Flask
from flask import jsonify, abort, request, session
import os
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User
from models import db_session


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
