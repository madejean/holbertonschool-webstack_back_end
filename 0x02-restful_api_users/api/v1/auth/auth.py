#!/usr/bin/python3
"""
creating API authentication
"""
from flask import Flask
from flask import request

class Auth():
     def require_auth(self, path, excluded_paths):
         if path is None or excluded_paths is None or path == [] or excluded_paths == []:
             return True
         if path in excluded_paths:
             return False
         if path == "/api/v1/status" or path == "/api/v1/status/" and path in excluded_paths:
             return False
         else:
             return True

     def authorization_header(self, request=None):
         return None

     def current_user(self, request=None):
         return None
