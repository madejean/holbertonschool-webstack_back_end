#!/usr/bin/python3
"""Unittest for User model"""
import unittest
import hashlib
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    """testing displays fullname of user"""
    def test_no_name_display(self):
        self.assertIs(self.user.display_name(), "")

    def test_email_display(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.assertIs(self.user.display_name(), "hbtn@holbertonschool.com")

    def test_firstname_display(self):
        self.user.first_name = "Bob"
        self.assertIs(self.user.display_name(), "Bob")

    def test_fullname_display(self):
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "Bob Dylan")

    """testing displays reformatted user info"""
    def test__str__(self):
        user = User()

    """testing password value"""
    def test_password(self):
        user = User()
