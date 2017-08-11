#!/usr/bin/python3
"""Unittest for User model"""
import unittest
import hashlib
from models.user import User


class TestUser(unittest.TestCase):
    """setUp user instance"""
    def setUp(self):
        self.user = User()

    """testing displays empty if no user"""
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
        self.assertEqual(self.user.display_name(), "Bob Dylan")

    """testing reformatted user info display"""
    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "[User] {} - {} - {}".format(
                self.user.id,
                self.user.email,
                self.user.display_name()
            )
        )

    """testing empty password"""
    def test_no_password(self):
        self.assertIsNone(self.user.password)

    """testing password value"""
    def test_password(self):
        self.user.password = "hello"
        self.assertEqual(self.user.password, "5d41402abc4b2a76b9719d911017c592")

    """testing password validatin"""
    def test_is_valid_password(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.user.password = "toto1234"
        self.assertFalse(self.user.is_valid_password(None))
