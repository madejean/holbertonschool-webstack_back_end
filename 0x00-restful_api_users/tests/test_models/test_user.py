#!/usr/bin/python3
import hashlib
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    def test_name_display(self):
        user = User()

    def test__str__(self):
        user = User()

    def test_password(self):
        user = User()

if __name__ == '__main__':
    unittest.main()
