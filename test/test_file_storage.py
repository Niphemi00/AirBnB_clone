#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for tests"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down after tests"""
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all returns the storage dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to the storage dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test that save properly serializes objects to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as f:
            data = json.load(f)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], obj.id)

    def test_reload(self):
        """Test that reload properly deserializes objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

if __name__ == '__main__':
    unittest.main()
