#!/usr/bin/python3
"""Module for FileStorage"""

import datetime
import json
import os


class FileStorage:

    """Class for storing data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects from obj"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as my_file:
            d = {k: val.to_dict() for k, val in FileStorage.__objects.items()}
            json.dump(d, my_file)

    def reload(self):
        """Reloads the objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding='utf-8') as my_file:
            obj_dict = json.load(my_file)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns a dict of classes that are valid"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.state import State

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Place": Place,
                   "Amenity": Amenity,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes for classnames"""
        attributes = {
                "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                "State":
                {"name": str},
                "City":
                {"state_id": str,
                    "name": str},
                "Place":
                {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "Amenity":
                {"name": str},
                "Review":
                {"place_id": str,
                    "user_d": str,
                    "text": str}

                }
        return attributes
