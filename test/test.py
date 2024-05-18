import unittest
import os
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models.base_model import BaseModel



class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_storage_is_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(FileStorage())
        key = "BaseModel.{}".format(FileStorage().id)
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        self.storage.new(FileStorage())
        self.storage.save()
        with open(self.file_path, "r") as f:
            self.assertIn("BaseModel", f.read())

    def test_reload(self):
        self.storage.new(FileStorage())
        self.storage.save()
        self.storage.reload()
        self.assertTrue(len(self.storage.all()) > 0)


class TestConsole(unittest.TestCase):
    def test_create(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertTrue(len(output) > 0)



class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_str_representation(self):
        obj = BaseModel()
        string = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), string)

if __name__ == "__main__":
    unittest.main()
