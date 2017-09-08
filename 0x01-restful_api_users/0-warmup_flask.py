#!/usr/bin/python3
"""
index route returns the string Holberton School
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def holberton_School():
    return 'Holberton School'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
