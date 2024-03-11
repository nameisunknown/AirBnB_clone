#!/usr/bin/python3
"""This module contains TestState class to test State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import os


class TestState(unittest.TestCase):
    """This class is for testing State class attributes and functions"""

    def test_instantiation(self):
        """Tests creating an instance of State class"""

        s1 = State()
        old_updated_at = s1.updated_at
        s1_dict = s1.to_dict()

        self.assertEqual(len(s1.id), 36)
        self.assertTrue(isinstance(s1, BaseModel))

        # Checking attributes types
        self.assertEqual(type(s1.id), str)
        self.assertEqual(type(s1.created_at), datetime)
        self.assertEqual(type(s1.updated_at), datetime)
        self.assertEqual(type(State.name), str)
        self.assertEqual(type(s1_dict["created_at"]), str)
        self.assertEqual(type(s1_dict["updated_at"]), str)

        self.assertLess(s1.created_at, s1.updated_at)

        # Checking __class__ attribute in __dict__ and to_dict()
        self.assertNotEqual(s1.created_at, old_updated_at)
        self.assertTrue("__class__" in s1_dict)
        self.assertTrue("__class__" not in s1.__dict__)

        # Creating a new instance using kwargs
        s2 = State(**s1_dict)

        self.assertTrue("__class__" in s2.to_dict())
        self.assertTrue("__class__" not in s2.__dict__)

        self.assertTrue(s2.to_dict()["__class__"], "BaseModel")

        # Checking datetime attributes types
        self.assertEqual(type(s2.created_at), datetime)
        self.assertEqual(type(s2.updated_at), datetime)

        # Checking if the two instances are the same object
        self.assertTrue(s1 is not s2)
        self.assertTrue(s1 != s2)

        # Checking if the two instance's attributes are equal
        self.assertEqual(s1.id, s2.id)
        self.assertEqual(s1.to_dict(), s2.to_dict())

        # Set new attribute to s2 instance
        s2.zip_code = "State 0xa7"
        self.assertNotEqual(s1.to_dict(), s2.to_dict())
        self.assertTrue("zip_code" in s2.to_dict())
        self.assertTrue("zip_code" not in s1.to_dict())

        # Tests that the each new created instance has a unique id
        s3 = State()
        self.assertNotEqual(s2.id, s3.id)
        self.assertEqual(len(s3.id), 36)

        self.assertLess(s1.created_at, s3.created_at)

    def test_save(self):
        """Tests (save) function"""
        s1 = State()
        old_updated_at = s1.updated_at

        self.assertTrue(not os.path.exists("file.json"))

        # Tests if updated_at attribute has changed after calling save() method
        s1.save()
        self.assertNotEqual(old_updated_at, s1.updated_at)

        self.assertTrue(os.path.exists("file.json"))

        with self.assertRaises(TypeError):
            s1.save(None)
        with self.assertRaises(TypeError):
            s1.save("None")
        with self.assertRaises(TypeError):
            s1.save(State())

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_str(self):
        """Tests __str__ function"""

        s1 = State()
        s1_str = f"[{s1.__class__.__name__}] ({s1.id}) {s1.__dict__}"
        self.assertEqual(s1.__str__(), s1_str)

        self.assertEqual(type(s1.__str__()), str)

        # Adding new attribute to change s1.__dict__
        s1.name = "State class"
        self.assertNotEqual(s1.__str__(), s1_str)

        with self.assertRaises(TypeError):
            s1.__str__(None)
        with self.assertRaises(TypeError):
            s1.__str__("None")

    def test_to_dict(self):
        """Tests to_dict function"""

        s1 = State()

        self.assertIn("name", State.__dict__.keys())

        self.assertNotIn("name", s1.to_dict())

        temp_dict1 = {'id': s1.id,
                      'created_at': s1.created_at.isoformat(),
                      'updated_at': s1.updated_at.isoformat(),
                      '__class__': s1.__class__.__name__
                      }

        self.assertEqual(s1.to_dict(), temp_dict1)
        self.assertNotEqual(s1.to_dict(), s1.__dict__)

        s1.name = "BaseModel class"
        self.assertNotEqual(s1.to_dict(), temp_dict1)

        temp_dict2 = {'id': s1.id,
                      'created_at': s1.created_at.isoformat(),
                      'updated_at': s1.updated_at.isoformat(),
                      '__class__': s1.__class__.__name__,
                      "name": "BaseModel class"}

        self.assertEqual(s1.to_dict(), temp_dict2)

        s1.name = "Test Man"
        self.assertIn("name", s1.to_dict())

        # Tests that created_at and updated_at from to_dict() function
        # Matching iso format
        self.assertEqual(s1.created_at,
                         datetime.fromisoformat(temp_dict1["created_at"]))

        self.assertEqual(s1.created_at,
                         datetime.strptime(temp_dict1["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

        self.assertEqual(s1.updated_at,
                         datetime.fromisoformat(temp_dict1["updated_at"]))

        self.assertEqual(s1.updated_at,
                         datetime.strptime(temp_dict1["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        with self.assertRaises(TypeError):
            s1.to_dict(None)
        with self.assertRaises(TypeError):
            s1.to_dict("None")
