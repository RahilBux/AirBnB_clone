#!/usr/bin/python3
"""Module for Base Model"""

import uuid
from datetime import datetime


class BaseModel:
    """Base class that other classes will inherit from"""

    def __init__(self):
        """Initialize instance
        Args:
            args: Variable number of arguments
            kwargs: Variable number of keyword arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str method to return string"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing all key-value pairs"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = type(self).__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
