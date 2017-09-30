#!/usr/bin/python3
"""
creating API authentication
"""
from flask import Flask
import sys

class Auth():
     def require_auth(self, path, excluded_paths):
         if path is None or excluded_paths is None:
             return True
         if path in excluded_paths:
             return False
         if path == "/api/v1/status" or path == "/api/v1/status/" and path in excluded_paths:
             return False
         else:
             return True

     def authorization_header(self, request=None):
         if request is None or request.headers['Authorization'] is None:
             return None
         else:
             return request.headers['Authorization']

     def current_user(self, request=None):
         return None
