from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models.user import User

@app_views.route('/users', strict_slashes=False)
def users():
    users = User.all()
    user_array = []
    for user in users:
        user_array.append(user.to_dict())
    return jsonify(user_array)
