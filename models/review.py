#!/usr/bin/python3
"""Module for review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class objects"""
    place_id = ""
    user_id = ""
    text = ""
