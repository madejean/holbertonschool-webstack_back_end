#!/usr/bin/python3
"""
creating flask instance
"""
from flask import Flask
from flask import jsonify, request, abort
import sys
import os
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from models import db_session

app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

"""registering the blueprint"""
app.register_blueprint(app_views, url_prefix="/api/v1")

@app.errorhandler(404)
def page_not_found(e):
    """
    returns error Not Found response
    """
    return jsonify(error="Not found"), 404


@app.errorhandler(401)
def request_unauthorized(e):
    """
    returns error Unauthorized response
    """
    return jsonify(error="Unauthorized"), 401


@app.errorhandler(403)
def request_Forbidden(e):
    """
    returns error Forbidden response
    """
    return jsonify(error="Forbidden"), 403


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database again at the end of the request.
    """
    db_session.remove()

@app.before_request
def before_request():
    auth = Auth()
    print(auth.require_auth(request.path, ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']), file=sys.stderr)
    if not auth.require_auth(request.path, ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']):
        print("THIS", file=sys.stderr)
        return None
    elif auth.authorization_header(request) is None:
        print("THAT", file=sys.stderr)
        return abort(401)
    elif auth.current_user(request) is None:
        print("MUCHOS", file=sys.stderr)
        return abort(403)


if __name__ == '__main__':
    app.run(port=HBNB_API_PORT, host=HBNB_API_HOST)
