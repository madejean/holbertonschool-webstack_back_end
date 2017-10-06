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
    """
        Creating BasicAuth class inheriting from Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header):
        """
            validates authorization header
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) != str:
            return None
        elif "Basic" not in authorization_header:
            return None
        else:
            return authorization_header.split("Basic ", 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """
            decodes base64 value
        """
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) != str:
            return None
        try:
            base64.b64decode(base64_authorization_header.encode('utf-8')
                ).decode('utf-8')

        except:
            return None
        else:
            return base64.b64decode(
                    base64_authorization_header.encode('utf-8')
                ).decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """
            retrieves decoded email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) != str:
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            email = decoded_base64_authorization_header.split(':')[0]
            index = decoded_base64_authorization_header.find(':')
            password = decoded_base64_authorization_header[index+1:]
            return email, password

    def user_object_from_credentials(self, user_email, user_pwd):
        """
            queries the database to get the user
        """
        from models import db_session
        if user_email is None or type(user_email) != str:
            return None
        elif user_email is None or type(user_pwd) != str:
            return None
        for user in db_session.query(User).filter(User.email == user_email):
            if not user:
                return None
            elif not user.is_valid_password(user_pwd):
                return None
            else:
                return user

    def current_user(self, request=None):
        """
            connecting all methods for Basic authentication
        """
        authorization_header = self.authorization_header(request)
        base64Val = self.extract_base64_authorization_header(
            authorization_header
        )
        decodedbase64 = self.decode_base64_authorization_header(base64Val)
        extracted_credentials = self.extract_user_credentials(decodedbase64)
        user_email = extracted_credentials[0]
        user_password = extracted_credentials[-1]
        retrieved_user = self.user_object_from_credentials(
            user_email, user_password
        )
        return retrieved_user
