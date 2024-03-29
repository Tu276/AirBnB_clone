#!/usr/bin/python3

"""
Defines the subclass: User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class is a subclass of BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
