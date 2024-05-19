#!/usr/bin/python3
"""Module for Base Model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class that other classes will inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize instance
        Args:
            args: Variable number of arguments
            kwargs: Variable number of keyword arguments
        """
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """str method to return string"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all key-value pairs"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = type(self).__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
