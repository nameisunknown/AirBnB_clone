#!/usr/bin/python3
"""
This module is for defining current folder as a package
and to declare a unique instance of FileStorage class
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
