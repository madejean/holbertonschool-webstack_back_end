#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

#defines index route
@app.route('/', methods=['GET'], strict_slashes=False)
def holberton_School():
    """
    index route returns the string Holberton School
    """
    return 'Holberton School'

#not executed when imported
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
