#!/usr/bin/python3

"""
Model and storage auto
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
