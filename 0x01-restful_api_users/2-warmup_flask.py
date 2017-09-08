from flask import Flask
import os

app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

@app.route('/', strict_slashes=False)
def holberton_School():
    return 'Holberton School'

@app.route('/c', strict_slashes=False)
def C_is_fun():
    return 'C is fun!'

if __name__ == '__main__':
    app.run(port=HBNB_API_PORT, host=HBNB_API_HOST)
