#!/usr/bin/python3
"""This module contains TestUser class to test User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import os


class TestUser(unittest.TestCase):
    """This class is for testing User class attributes and functions"""

    def test_instantiation(self):
        """Tests creating an instance of User class"""

        u1 = User()
        old_updated_at = u1.updated_at
        u1_dict = u1.to_dict()

        self.assertEqual(len(u1.id), 36)
        self.assertTrue(isinstance(u1, BaseModel))

        # Checking attributes types
        self.assertEqual(type(u1.id), str)
        self.assertEqual(type(u1.created_at), datetime)
        self.assertEqual(type(u1.updated_at), datetime)
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)
        self.assertEqual(type(u1_dict["created_at"]), str)
        self.assertEqual(type(u1_dict["updated_at"]), str)

        self.assertLess(u1.created_at, u1.updated_at)

        # Checking __class__ attribute in __dict__ and to_dict()
        self.assertNotEqual(u1.created_at, old_updated_at)
        self.assertTrue("__class__" in u1_dict)
        self.assertTrue("__class__" not in u1.__dict__)

        # Creating a new instance using kwargs
        u2 = User(**u1_dict)

        self.assertTrue("__class__" in u2.to_dict())
        self.assertTrue("__class__" not in u2.__dict__)

        self.assertTrue(u2.to_dict()["__class__"], "BaseModel")

        # Checking datetime attributes types
        self.assertEqual(type(u2.created_at), datetime)
        self.assertEqual(type(u2.updated_at), datetime)

        # Checking if the two instances are the same object
        self.assertTrue(u1 is not u2)
        self.assertTrue(u1 != u2)

        # Checking if the two instance's attributes are equal
        self.assertEqual(u1.id, u2.id)
        self.assertEqual(u1.to_dict(), u2.to_dict())

        # Set new attribute to u2 instance
        u2.name = "User class"
        self.assertNotEqual(u1.to_dict(), u2.to_dict())
        self.assertTrue("name" in u2.to_dict())
        self.assertTrue("name" not in u1.to_dict())

        # Tests that the each new created instance has a unique id
        u3 = User()
        self.assertNotEqual(u2.id, u3.id)
        self.assertEqual(len(u3.id), 36)

        self.assertLess(u1.created_at, u3.created_at)

    def test_save(self):
        """Tests (save) function"""
        u1 = User()
        old_updated_at = u1.updated_at

        self.assertTrue(not os.path.exists("file.json"))

        # Tests if updated_at attribute has changed after calling save() method
        u1.save()
        self.assertNotEqual(old_updated_at, u1.updated_at)

        self.assertTrue(os.path.exists("file.json"))

        with self.assertRaises(TypeError):
            u1.save(None)
        with self.assertRaises(TypeError):
            u1.save("None")
        with self.assertRaises(TypeError):
            u1.save(User())

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_str(self):
        """Tests __str__ function"""

        u1 = User()
        u1_str = f"[{u1.__class__.__name__}] ({u1.id}) {u1.__dict__}"
        self.assertEqual(u1.__str__(), u1_str)

        self.assertEqual(type(u1.__str__()), str)

        # Adding new attribute to change u1.__dict__
        u1.name = "User class"
        self.assertNotEqual(u1.__str__(), u1_str)

        with self.assertRaises(TypeError):
            u1.__str__(None)
        with self.assertRaises(TypeError):
            u1.__str__("None")

    def test_to_dict(self):
        """Tests to_dict function"""

        u1 = User()
        user_attributes = [
            "email",
            "password",
            "first_name",
            "last_name"
        ]

        for attr in user_attributes:
            self.assertIn(attr, User.__dict__.keys())

        for attr in user_attributes:
            self.assertNotIn(attr, u1.to_dict())

        temp_dict1 = {'id': u1.id,
                      'created_at': u1.created_at.isoformat(),
                      'updated_at': u1.updated_at.isoformat(),
                      '__class__': u1.__class__.__name__
                      }

        self.assertEqual(u1.to_dict(), temp_dict1)
        self.assertNotEqual(u1.to_dict(), u1.__dict__)

        u1.name = "BaseModel class"
        self.assertNotEqual(u1.to_dict(), temp_dict1)

        temp_dict2 = {'id': u1.id,
                      'created_at': u1.created_at.isoformat(),
                      'updated_at': u1.updated_at.isoformat(),
                      '__class__': u1.__class__.__name__,
                      "name": "BaseModel class"}

        self.assertEqual(u1.to_dict(), temp_dict2)

        u1.first_name = "test"
        self.assertIn("first_name", u1.to_dict())

        # Tests that created_at and updated_at from to_dict() function
        # Matching iso format
        self.assertEqual(u1.created_at,
                         datetime.fromisoformat(temp_dict1["created_at"]))

        self.assertEqual(u1.created_at,
                         datetime.strptime(temp_dict1["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

        self.assertEqual(u1.updated_at,
                         datetime.fromisoformat(temp_dict1["updated_at"]))

        self.assertEqual(u1.updated_at,
                         datetime.strptime(temp_dict1["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        with self.assertRaises(TypeError):
            u1.to_dict(None)
        with self.assertRaises(TypeError):
            u1.to_dict("None")
