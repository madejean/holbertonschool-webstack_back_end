#!/usr/bin/python3
"""
creating Basic authentication
"""
from flask import Flask
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    pass
