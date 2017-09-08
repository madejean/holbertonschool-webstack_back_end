#!/usr/bin/python3
"""
endpoint returns a json structure
"""
from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')


@app.route('/', strict_slashes=False)
def holberton_School():
    """
    returns the string Holberton School
    """
    return 'Holberton School'


@app.route('/c', strict_slashes=False)
def C_is_fun():
    """
    returns the string C is fun!
    """
    return 'C is fun!'


@app.route('/hbtn', strict_slashes=False)
def hbtn():
    """
    returns a json structure
    """
    return jsonify(C="is fun", Python="is cool", Sysadmin="is hiring")

if __name__ == '__main__':
    app.run(port=HBNB_API_PORT, host=HBNB_API_HOST)
