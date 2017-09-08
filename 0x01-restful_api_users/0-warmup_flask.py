#!/usr/bin/python3
"""
    index route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holberton_School():
    """
    returns the string C is fun!
    """
    return 'Holberton School'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
