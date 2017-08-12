#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """setUp model"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_not_none(self):
        
        """
        testing values are not none
        """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)

    def test_id(self):
        """
        testing instances
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_unique_id(self):

        """
        testing id unique
        """
        id_1 = BaseModel().id
        id_2 = BaseModel().id
        self.assertNotEqual(id_1, id_2)

    def test_created_at(self):

        """
        testing created_at
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):

        """
        testing updated_at
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)
