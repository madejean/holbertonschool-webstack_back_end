#!/usr/bin/python3
"""
Unittest for User model
"""
import unittest
import hashlib
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        """
        setUp user instance
        """
        self.user = User()
        self.dict_user = User()
        self.dict_user.email = "hbtn@holbertonschool.com"
        self.dict_user.password = "toto1234"
        self.dict_user.first_name = "Bob"
        self.dict_user.last_name = "Dylan"
        self.d_user = self.dict_user.to_dict()

    # Testing display_name()
    def test_no_value_display(self):
        """
        testing displays empty if no user
        """
        self.assertIs(self.user.display_name(), "")

    # Testing display_name()
    def test_email_display(self):
        """
        testing email value display
        """
        self.user.email = "hbtn@holbertonschool.com"
        self.assertIs(self.user.display_name(), "hbtn@holbertonschool.com")

    # Testing display_name()
    def test_firstname_display(self):
        """
        testing first name value display
        """
        self.user.first_name = "Bob"
        self.assertIs(self.user.display_name(), "Bob")

    # Testing display_name()
    def test_lastname_display(self):
        """
        testing last name value display
        """
        self.user.email = "test@hotmail.com"
        self.user.last_name = "Dylan"
        self.assertIs(self.user.display_name(), "Dylan")

    # Testing display_name()
    def test_fullname_display(self):
        """
        testing full name value display
        """
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "Bob Dylan")

    def test__str__(self):
        """
        testing reformatted user info display
        """
        self.assertEqual(
            self.user.__str__(),
            "[User] {} - {} - {}".format(
                self.user.id,
                self.user.email,
                self.user.display_name()
            )
        )

    def test_no_password(self):
        """
        testing empty password
        """
        self.assertIsNone(self.user.password)

    def test_password(self):
        """
        testing password value
        """
        self.user.password = "hello"
        self.assertEqual(
            self.user.password,
            "5d41402abc4b2a76b9719d911017c592"
        )

    def test_is_valid_password_none(self):
        """
        testing password None
        """
        self.assertFalse(self.user.is_valid_password(None))

    def test_password_is_not_valid(self):
        """
        testing false password
        """
        self.assertFalse(self.user.is_valid_password(89))
        self.assertFalse(self.user.is_valid_password("tutu1234"))

    def test_password_is_valid(self):
        """
        testing valid password
        """
        self.user.email = "hbtn@holbertonschool.com"
        self.user.password = "toto1234"
        self.assertTrue(self.user.is_valid_password("toto1234"))

    def test_id_to_dict_id(self):
        """
        testing id in dict
        """
        self.assertIsInstance(self.d_user["id"], str)

    def test_to_dict_updated_at(self):
        """
        testing updated_at in dict
        """
        self.assertIsInstance(dict["updated_at"], str)


    def test_to_dict_firstname(self):
        """
        testing first_name in dict
        """
        self.assertIsInstance(dict["first_name"], str)


    def test_to_dict_email(self):
        """
        testing email in dict
        """
        self.assertIsInstance(dict["email"], str)

    def test_to_dict_lastname(self):
        """
        testing last_name in dict
        """
        self.assertIsInstance(dict["last_name"], str)


    def test_to_dict_created_at(self):
        """
        testing created_at in dict
        """
        self.assertIsInstance(dict["created_at"], str)
