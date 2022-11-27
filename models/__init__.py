#!/usr/bin/python3

"""
Model and storage auto
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
