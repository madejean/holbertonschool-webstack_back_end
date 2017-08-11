#!/usr/bin/python3
"""Unittest for User model"""
import unittest
import hashlib
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """testing displays fullname of user"""
    def test_name_display(self):
        user = User()

    """testing displays reformatted user info"""
    def test__str__(self):
        user = User()

    """testing password value"""
    def test_password(self):
        user = User()
