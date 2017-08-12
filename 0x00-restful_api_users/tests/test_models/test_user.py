#!/usr/bin/python3
import unittest
import hashlib
from models.user import User

class Test_user(unittest.TestCase):
    def setUp(self):
        self.none_user = User()
        self.user = User()
        self.dict_user = User()
        self.dict_user.email = "hbtn@holbertonschool.com"
        self.dict_user.password = "toto1234"
        self.dict_user.first_name = "Bob"
        self.dict_user.last_name = "Dylan"

    def test_first_name(self):
        self.user.first_name = "Bob"
        self.assertEqual(self.user.display_name(), "Steven")

    def test_last_name(self):
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "Garcia")

    def test_email(self):
        self.user.email = "bobDylan@hotmail.com"
        self.assertEqual(self.user.display_name(), "steven@gmail.com")

    def test_first_last_name(self):
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertEqual(self.user.display_name(), "Steven Garcia")

    def test_none(self):
        self.assertEqual(self.none_user.display_name(), "")

    def test_str_email(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.assertIn("- hbtn@holbertonschool.com - hbtn@holbertonschool.com",
                      str(self.user))

    def test_str_first_last_name(self):
        self.user.email = "hbtn@holbertonschool.com"
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertIn("- hbtn@holbertonschool.com - Bob Dylan", str(self.user))

    def test_str_none(self):
        '''
            testing _str_none
        '''
        self.assertIn("- None - ", str(self.user))

    def test_str_none_email(self):
        '''
            Testing _str_none_email
        '''
        self.user.first_name = "Bob"
        self.user.last_name = "Dylan"
        self.assertIn("- None - Bob Dylan", str(self.user))

    def test_password_encription(self):
        self.user.password = "hello"
        string = hashlib.sha224(b"hello").hexdigest()
        self.assertEqual(string, self.user.password)

    def test_none_password(self):
        self.assertEqual(None, self.user.password)

    def test_not_str_password(self):
        self.user.password = 124324
        self.assertEqual(None, self.user.password)

    def test_pwd_none(self):
        self.user.password = "toto1234"
        validator = self.user.is_valid_password(None)
        self.assertFalse(validator)

    def test__pasword_none(self):
        self.user.password = None
        validator = self.user.is_valid_password("toto1234")
        self.assertFalse(validator)

    def test_pwd_type(self):
        self.user.password = "hello"
        validator = self.user.is_valid_password(89)
        self.assertFalse(validator)

    def test_pwd__password_not_equal(self):
        self.user.password = "hello"
        validator = self.user.is_valid_password("hi")
        self.assertFalse(validator)

    def test_pwd_password_equal(self):
        self.user.password = "hello"
        validator = self.user.is_valid_password("hello")
        self.assertTrue(validator)


    def test_id_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["id"], str)

    def test_email_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["email"], str)

    def test_first_name_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["first_name"], str)

    def test_last_name_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["last_name"], str)

    def test_updated_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["updated_at"], str)

    def test_created_type(self):
        dict = self.dict_user.to_dict()
        self.assertIsInstance(dict["created_at"], str)
