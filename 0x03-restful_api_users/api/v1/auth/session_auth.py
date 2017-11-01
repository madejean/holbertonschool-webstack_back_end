#!/usr/bin/python3
"""
creating Basic authentication
"""
from flask import Flask, jsonify, abort, request
from api.v1.auth.auth import Auth
from models.user import User
from models import db_session
import uuid


class SessionAuth(Auth):
    """
        Creating Session class inheriting from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        if user_id is None or type(user_id) != str:
            return None
        else:
            sessionID = str(uuid.uuid4())
            self.user_id_by_session_id[sessionID] = user_id
            return sessionID

    def user_id_for_session_id(self, session_id=None):
        if session_id is None or type(session_id) != str:
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return abort(403)
        user = db_session.query(User).get(user_id)
        return user

    def destroy_session(self, request=None):
        print(self.session_cookie(request))
        if request is None:
            return False
        if self.session_cookie(request) is None:
            return False
        if self.user_id_for_session_id(self.session_cookie(request)) is None:
            return False
        else:
            del self.user_id_by_session_id[self.session_cookie(request)]
            return True
