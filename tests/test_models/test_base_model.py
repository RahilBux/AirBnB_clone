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

    def test_new_instance_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_two_models_ids_unique(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_two_models_diff_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_str_rep(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        base1 = BaseModel()
        base1.id = "123456"
        base1.created_at = base1.updated_at = date_time
        basestr = base1.__str__()
        self.assertIn("[BaseModel] (123456)", basestr)
        self.assertIn("'id': '123456'", basestr)
        self.assertIn("'created_at': " + date_time_repr, basestr)
        self.assertIn("'updated_at': " + date_time_repr, basestr)

    def test_unused_args(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_init_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base = BaseModel(id="123", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.updated_at, date_time)

    def test_init_nokwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_kwargs_and_args(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base = BaseModel(id="123", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.updated_at, date_time)

if __name__ == "__main__":
    unittest.main()
