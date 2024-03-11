#!/usr/bin/python3
"""This module contains FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """
    This class is for serializing instances to a JSON file
    and deserializing JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary (__objects)"""

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)

        Args:
        obj (dict): Is the dict representaion of the object to add to
        (__objects) dictionary
        """

        obj_key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w") as file:
            serialized_objects = {}
            for key, value in FileStorage.__objects.items():
                serialized_objects[key] = value.to_dict()
            json.dump(serialized_objects, file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists, otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
