#!/usr/bin/python3
"""Unittest for file_storage"""
import os
import models
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_init(unittest.TestCase):
    """Unittest to perform"""

    def test_FileStorage_init_noargs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

if __name__ == "__main__":
    unittest.main()
