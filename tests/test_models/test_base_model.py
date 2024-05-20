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
        base = BaseModel(id="123",
                         created_at=date_time_iso,
                         updated_at=date_time_iso)
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.updated_at, date_time)

    def test_init_nokwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_kwargs_and_args(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base = BaseModel(id="123",
                         created_at=date_time_iso,
                         updated_at=date_time_iso)
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.updated_at, date_time)


class TestBaseModelsave(unittest.TestCase):
    """Unittest for save method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, basemodel.updated_at)

    def test_two_saves(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_update = basemodel.updated_at
        basemodel.save()
        second_update = basemodel.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        basemodel.save()
        self.assertLess(second_update, basemodel.updated_at)

    def test_save_args(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_save_update_file(self):
        basemodel = BaseModel()
        basemodel.save()
        basemodelid = "BaseModel." + basemodel.id
        with open("file.json", "r") as file:
            self.assertIn(basemodelid, file.read())


class TestBaseModel_todict(unittest.TestCase):
    """Test the to dict method"""

    def test_to_dict(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_added_attributes(self):
        base = BaseModel()
        base.name = "John"
        base.my_number = 21
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime_str(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_to_dict_out(self):
        dt = datetime.today()
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = dt
        todict = {
                'id': '123456',
                '__class__': 'BaseModel',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(base.to_dict(), todict)

    def test_contrast_to_dict(self):
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)

    def test_to_dict_args(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
