#!/usr/bin/python3
"""
route /c
"""
from flask import Flask

app = Flask(__name__)


@app.route('/c', strict_slashes=False)
def C_is_fun():
    """
    returns the string C is fun!
    """
    return 'C is fun!'

"""not executed when imported"""
if __name__ == '__main__':
    app.run()
