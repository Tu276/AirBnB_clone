#!/usr/bin/python3
"""
Subclass Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class is a subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
