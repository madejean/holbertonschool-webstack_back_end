#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


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

    """testing created_at values"""
    def test_created_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.created_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )

    """testing updated_at values"""
    def test_updated_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.updated_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )

if __name__ == '__main__':
    unittest.main()
