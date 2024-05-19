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

        classes = {"BaseModel": BaseModel}
        return classes

    def attributes(self):
        """Returns the valid attributes for classnames"""
        attributes = {
                "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime}
                    }
        return attributes
