#!/usr/bin/python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models import db_session
from models.user import User

""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user))
db_session.add(user)
db_session.commit()

""" Retreive this user via the class BasicAuth """

a = BasicAuth()

print(a.user_object_from_credentials(None, None))
print(a.user_object_from_credentials(89, 98))
print(a.user_object_from_credentials("email@notfound.com", "pwd"))
print(a.user_object_from_credentials(user_email, "pwd"))
print(a.user_object_from_credentials(user_email, user_clear_pwd))
