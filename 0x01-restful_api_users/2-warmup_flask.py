#!/usr/bin/python3
"""
defining some routes
"""
from flask import Flask
import os

app = Flask(__name__)

"""retrieving port and host from environment variables"""
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

"""run the app through host and port"""
if __name__ == '__main__':
    app.run(port=HBNB_API_PORT, host=HBNB_API_HOST)
