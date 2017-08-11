#!/usr/bin/python3
"""Unittest for User model"""
import unittest
import hashlib
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """setUp user instance"""
    def setUp(self):
        self.user = User()

    """testing displays fullname of user"""
    def test_no_name_display(self):
        self.assertIs(self.user.display_name(), "")

    """testing email value display"""
    def test_email_display(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.assertIs(self.user.display_name(), "hbtn@holbertonschool.com")

    """testing first name value display"""
    def test_firstname_display(self):
        self.user.first_name = "Bob"
        self.assertIs(self.user.display_name(), "Bob")

    """testing last name value display"""
    def test_lastname_display(self):
        self.user.email = "test@hotmail.com"
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "Dylan")

    """testing full name value display"""
    def test_fullname_display(self):
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "{} {}".format(self.user.first_name, self.user.last_name))

    """testing reformatted user info display"""
    def test__str__(self):
        self.assertEqual(self.user.__str__(), "[User] {} - {} - {}".format(self.user.id, self.user.email, self.user.display_name()))

    """testing password value"""
    def test_password(self):
        user = User()
