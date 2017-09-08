#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def holberton_School():
    """
        index route returns the string Holberton School
    """
    app.url_map.strict_slashes = False
    return 'Holberton School'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
