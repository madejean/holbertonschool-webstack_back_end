#!/usr/bin/python3
"""
Test link to MySQL database
"""
from models import db_session
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
user.password = "toto1234"
print("New user: {}".format(user))
db_session.add(user)
db_session.commit()

<<<<<<< HEAD
=======

>>>>>>> 8f86ee2c8f668c5620f6997bc923176e9146c650
user2 = User()
user2.email = "hbtn2@holbertonschool.com"
user2.password = "toto1234"
print("New user: {}".format(user2))
db_session.add(user2)
db_session.commit()

<<<<<<< HEAD
=======

>>>>>>> 8f86ee2c8f668c5620f6997bc923176e9146c650
print("All users:")
for user in db_session.query(User).all():
    print(user)
