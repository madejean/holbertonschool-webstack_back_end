#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


"""
    index route returns the string Holberton School
"""
@app.route('/', methods=['GET'], strict_slashes=False)
def holberton_School():
    return 'Holberton School'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
