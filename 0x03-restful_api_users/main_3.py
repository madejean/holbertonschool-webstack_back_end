#!/usr/bin/python3
""" Main 3
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(sa.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
