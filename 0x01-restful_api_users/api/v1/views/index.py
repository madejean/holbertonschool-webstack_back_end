from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models.base_model import count

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify(status="OK")

@app_views.route('/stats', strict_slashes=False)
def stats():
    return jsonify(users=count)
