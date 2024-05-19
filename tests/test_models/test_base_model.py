#!/usr/bin/python3
"""Python test scripts for base_model"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_basemodel_init(unittest.TestCase):
    """Unittests for testing the init method"""

    def test_no_args_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_public(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

if __name__ == "__main__":
    unittest.main()
