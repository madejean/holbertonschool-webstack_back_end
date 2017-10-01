#!/usr/bin/python3
"""
creating Basic authentication
"""
from flask import Flask
from api.v1.auth.auth import Auth
from models.user import User
from models import db_session
import base64

class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header):
        if authorization_header is None or type(authorization_header) != str or not "Basic" in authorization_header:
            return None
        else:
            return authorization_header.split()[-1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        if base64_authorization_header is None or type(base64_authorization_header) != str:
            return None
        try:
            if base64.b64decode(base64_authorization_header):
                return base64.b64decode(base64_authorization_header).decode('utf-8')
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) != str or not ":" in decoded_base64_authorization_header:
            return None, None
        else:
            email = decoded_base64_authorization_header.split(':')[0]
            password = decoded_base64_authorization_header.split(':')[-1]
            return email, password

    def user_object_from_credentials(self, user_email, user_pwd):
        if user_email is None or user_pwd is None or type(user_email) != str or type(user_pwd) != str:
            return None
        from models import db_session
        user = db_session.query(User).filter(User.email == user_email)
        print("THIS {}".format(user))
        """if user is None or user.is_valid_password(user_pwd) is False:
            return None"""
        """else:
            return user"""
