#!/usr/bin/python3
"""Unittest for the User class"""
import os
import models
import unittest
from models.place import Place
from datetime import datetime
from time import sleep


class TestUser_init(unittest.TestCase):
    """Unittest for init of class"""

    def test_no_args_init(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_and_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        state = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(state))
        self.assertNotIn("city_id", state.__dict__)

    def test_user_id_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)
    
    def test_name_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_description_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_number_of_rooms_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_two_place_ids(self):
        state1 = Place()
        state2 = Place()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_users_created_at(self):
        state1 = Place()
        sleep(0.05)
        state2 = Place()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_users_updated_at(self):
        user1 = Place()
        sleep(0.05)
        user2 = Place()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = Place()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        userstr = user.__str__()
        self.assertIn("[Place] (123456)", userstr)
        self.assertIn("'id': '123456'", userstr)
        self.assertIn("'created_at': " + dt_repr, userstr)
        self.assertIn("'updated_at': " + dt_repr, userstr)

    def test_args_not_used(self):
        user = Place(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_init_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.updated_at, dt)
        self.assertEqual(user.created_at, dt)

    def test_init_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


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
        user = Place()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_args(self):
        user = Place()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_update_file(self):
        user = Place()
        user.save()
        userid = "Place." + user.id
        with open("file.json", "r") as file:
            self.assertIn(userid, file.read())


class TestUser_to_dictionary(unittest.TestCase):
    """Unittest for testing the to_dict method"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_correct_keys(self):
        user = Place()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_any_added_attributes(self):
        user = Place()
        user.middle_name = "John"
        user.my_number = 11
        self.assertEqual("John", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_str(self):
        user = Place()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = Place()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        todict = {
                'id': '123456',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(user.to_dict(), todict)

    def test_contrast_to_dict(self):
        user = Place()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_args(self):
        user = Place()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
