#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

"""
route /c returns the string C is fun!
"""


@app.route('/c', strict_slashes=False)
def C_is_fun():
    return 'C is fun!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
