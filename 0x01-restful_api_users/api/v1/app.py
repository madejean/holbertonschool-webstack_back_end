#!/usr/bin/python3
"""
creating flask instance
"""
from flask import Flask
from flask import jsonify
import os
from .views import app_views
from models import db_session

app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

"""registering the blueprint"""
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(e):
    """
    returns error response
    """
    return jsonify(error="Not found"), 404


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database again at the end of the request.
    """
    db_session.remove()

if __name__ == '__main__':
    app.run(port=HBNB_API_PORT, host=HBNB_API_HOST)
