#!/usr/bin/python3
"""This is the module for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
