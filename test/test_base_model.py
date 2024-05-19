#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_save(self):
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, old_updated_at)

    def test_to_dict(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
