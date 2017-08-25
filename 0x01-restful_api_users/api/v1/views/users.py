from flask import Flask
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User
from models import db_session

@app_views.route('/users', strict_slashes=False)
def users():
    users = User.all()
    user_array = []
    for user in users:
        user_array.append(user.to_dict())
    return jsonify(user_array)

@app_views.route('/users/<user_id>', strict_slashes=False)
def user(user_id):
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        d_user = user.to_dict()
        return jsonify(d_user)

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        db_session.commit()
        return jsonify()
