#!/usr/bin/python3
"""Unittest for the User class"""
import os
import models
import unittest
from models.city import City
from datetime import datetime
from time import sleep


class TestUser_init(unittest.TestCase):
    """Unittest for init of class"""

    def test_no_args_init(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_and_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_public_class_attribute(self):
        state = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(state))
        self.assertNotIn("state_id", state.__dict__)

    def test_name_is_public_class(self):
        city = City()
        self.assertEqual(str, type(City().name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_state_ids(self):
        state1 = City()
        state2 = City()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_users_created_at(self):
        state1 = City()
        sleep(0.05)
        state2 = City()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_users_updated_at(self):
        user1 = City()
        sleep(0.05)
        user2 = City()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = City()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        userstr = user.__str__()
        self.assertIn("[City] (123456)", userstr)
        self.assertIn("'id': '123456'", userstr)
        self.assertIn("'created_at': " + dt_repr, userstr)
        self.assertIn("'updated_at': " + dt_repr, userstr)

    def test_args_not_used(self):
        user = City(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_init_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.updated_at, dt)
        self.assertEqual(user.created_at, dt)

    def test_init_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittest for testing the save method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        user = City()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_args(self):
        user = City()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_update_file(self):
        user = City()
        user.save()
        userid = "City." + user.id
        with open("file.json", "r") as file:
            self.assertIn(userid, file.read())


class TestUser_to_dictionary(unittest.TestCase):
    """Unittest for testing the to_dict method"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_correct_keys(self):
        user = City()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_any_added_attributes(self):
        user = City()
        user.middle_name = "John"
        user.my_number = 11
        self.assertEqual("John", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_str(self):
        user = City()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = City()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        todict = {
                'id': '123456',
                '__class__': 'City',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(user.to_dict(), todict)

    def test_contrast_to_dict(self):
        user = City()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_args(self):
        user = City()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
