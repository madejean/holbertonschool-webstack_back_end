#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        self.assertIsNone(BaseModel.id)
        self.assertIsNone(BaseModel.created_at)
        self.assertIsNone(BaseModel.updated_at)

    def test_unique_id(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, uuid.UUID))

    def test_created_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.created_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )

    def test_updated_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, str)
        self.assertIsInstance(
            datetime.strptime(base_model.updated_at, "%Y-%m-%d %H:%M:%S.%f"),
            datetime
        )

if __name__ == '__main__':
    unittest.main()
