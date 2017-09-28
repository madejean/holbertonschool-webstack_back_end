#!/usr/bin/python3
"""
creating status routes
"""
from flask import Flask
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    returns OK status
    """
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    returns user count
    """
    return jsonify(users=User.count())

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """
    aborts on 401 status code
    """
    return abort(401)
