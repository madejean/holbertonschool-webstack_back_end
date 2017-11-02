#!/usr/bin/python3
"""
creating API authentication
"""
from flask import Flask, request
import os

HBNB_YELP_SESSION_NAME = os.environ.get('HBNB_YELP_SESSION_NAME')


class Auth():
    """
        Creating Auth parent class
    """
    def require_auth(self, path, excluded_paths):
        """
            filter routes that do not need auth
        """
        if path is None:
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        elif not path.endswith('/'):
            path = path + '/'
        if path in excluded_paths:
            return False
        elif path == "/api/v1/status" or path == "/api/v1/status/":
            return False
        else:
            return True

    def authorization_header(self, request=None):
        """
            validates request authentication
        """
        if request is None:
            return None
        elif request.headers.get('Authorization') is None:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None):
        """
            defined in Basic Auth child class
        """
        return None

    def session_cookie(self, request=None):
        """
            method to get session cookie
        """
        if request is None:
            return None
        return request.cookies.get(HBNB_YELP_SESSION_NAME)
