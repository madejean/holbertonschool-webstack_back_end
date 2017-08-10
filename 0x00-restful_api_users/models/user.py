#!/usr/bin/python3
import hashlib
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel, Base):
    __tablename__  = 'users'
    email = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    _password = Column(String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if password is None or not isinstance(password, str):
            self._password = None
        else:
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            self._password = m.hexdigest().lower()

    def display_name(self):
        if self.email is None and self.first_name is None and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return self.email
        if self.last_name is None:
            return self.first_name
        if self.first_name is None:
            print self.last_name
        else:
            return("{} {}".format(self.first_name, self.last_name))

    def __str__(self):
        return("[User] {} - {} - {}".format(self.id, self.email, self.display_name()))

    def is_valid_password(self, pwd):
        if pwd is None or not isinstance(pwd, str) or self._password is None:
            return False
        m = hashlib.md5()
        m.update(pwd)
        md5_pwd = m.hexdigest().lower()
        if md5_pwd == self._password:
            return True
        else:
            return False

    def to_dict(self):
        d_user = {
            "id": str(self.id),
            "email": str(self.email),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "created_at": str(datetime.strftime(self.created_at, "%Y-%m-%d %H:%M:%S")),
            "updated_at": str(datetime.strftime(self.updated_at, "%Y-%m-%d %H:%M:%S"))
        }
        return d_user
