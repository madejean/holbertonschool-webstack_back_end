#!/usr/bin/python3
"""Unittest for User model"""
import unittest
import hashlib
from models.user import User


class TestUser(unittest.TestCase):
    """setUp user instance"""
    def setUp(self):
        self.user = User()
        self.dict_user = User()
        self.dict_user.email = "hbtn@holbertonschool.com"
        self.dict_user.password = "toto1234"
        self.dict_user.first_name = "Bob"
        self.dict_user.last_name = "Dylan"
        self.d_user = self.dict_user.to_dict()

    """testing displays empty if no user"""
    def test_no_value_display(self):
        self.assertEqual(self.user.display_name(), "")

    """testing email value display"""
    def test_email_display(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.user.display_name(), "hbtn@holbertonschool.com")

    """testing first name value display"""
    def test_firstname_display(self):
        self.user.first_name = "Bob"
        self.assertEqual(self.user.display_name(), "Bob")

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
        self.assertEqual(
            self.user.password,
            "5d41402abc4b2a76b9719d911017c592"
        )

    """testing password None"""
    def test_is_valid_password_none(self):
        self.assertFalse(self.user.is_valid_password(None))

    """testing false password"""
    def test_password_is_not_valid(self):
        self.assertFalse(self.user.is_valid_password(89))
        self.assertFalse(self.user.is_valid_password("tutu1234"))

    """testing valid password"""
    def test_password_is_valid(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.user.password = "toto1234"
        self.assertTrue(self.user.is_valid_password("toto1234"))

    """testing id in dict"""
    def test_id_to_dict_id(self):
        self.assertIsInstance(self.d_user["id"], str)

    """testing updated_at in dict"""
    def test_to_dict_updated_at(self):
        self.assertEqual(
            "{} ({})".format("updated_at", type(self.d_user["updated_at"])),
            "updated_at (<class 'str'>)"
        )

    """testing first_name in dict"""
    def test_to_dict_firstname(self):
        self.assertEqual(
            "{} ({}): {}".format(
                "first_name",
                type(self.d_user["first_name"]),
                self.dict_user.first_name
            ),
            "first_name (<class 'str'>): Bob"
        )

    """testing email in dict"""
    def test_to_dict_email(self):
        self.assertEqual(
            "{} ({}): {}".format(
                "email",
                type(self.d_user["email"]),
                self.dict_user.email
            ),
            "email (<class 'str'>): hbtn@holbertonschool.com"
        )

    """testing last_name in dict"""
    def test_to_dict_lastname(self):
        self.assertEqual(
            "{} ({}): {}".format(
                "last_name",
                type(self.d_user["last_name"]),
                self.dict_user.last_name
            ),
            "last_name (<class 'str'>): Dylan"
        )

    """testing created_at in dict"""
    def test_to_dict_created_at(self):
        self.assertEqual(
            "{} ({})".format("created_at", type(self.d_user["created_at"])),
            "created_at (<class 'str'>)"
        )
