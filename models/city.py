#!/usr/bin/python3
"""
Module subclass City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Null ref BaseModel
    """
    state_id = ""
    name = ""
