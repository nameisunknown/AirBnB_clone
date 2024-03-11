#!/usr/bin/python3
""" this module in the Base model class module """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes instances of the class

        Args:
            args (list): A list that conttains all
            the attributes of the new instance to create

            kwargs (dict): A dictionary that conttains all
            the attributes of the new instance to create
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the class"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        (updated_at) with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        # Get all instance attributes
        # copy is used to create a copy, without it we'd create a refrence
        obj_dict = self.__dict__.copy()

        # Add __class__ attribute
        obj_dict["__class__"] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
