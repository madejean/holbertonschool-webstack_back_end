#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from models.base_model import BaseModel

<<<<<<< HEAD

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    """testing values are not none"""
    def test_not_none(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)

    """testing instances"""
    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)
=======

class TestBaseModel(unittest.TestCase):
    """testing intial values"""
    def test_initialization(self):
        self.assertIsNone(BaseModel.id)
        self.assertIsNone(BaseModel.created_at)
        self.assertIsNone(BaseModel.updated_at)

    """testing for unique ids"""
    def test_unique_id(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, uuid.UUID))
>>>>>>> b2c8a6fd67d9f40641b403c16c96cc85870ad4c3

    """testing created_at values"""
    def test_created_at(self):
<<<<<<< HEAD
        self.assertIsInstance(self.base_model.created_at, datetime)
=======
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.created_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )
>>>>>>> b2c8a6fd67d9f40641b403c16c96cc85870ad4c3

    """testing updated_at values"""
    def test_updated_at(self):
<<<<<<< HEAD
        self.assertIsInstance(self.base_model.updated_at, datetime)
=======
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.updated_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )

if __name__ == '__main__':
    unittest.main()
>>>>>>> b2c8a6fd67d9f40641b403c16c96cc85870ad4c3
