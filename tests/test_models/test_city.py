#!/usr/bin/python3
"""This module contains TestCity class to test City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import os


class TestCity(unittest.TestCase):
    """This class is for testing City class attributes and functions"""

    def test_instantiation(self):
        """Tests creating an instance of City class"""

        c1 = City()
        old_updated_at = c1.updated_at
        c1_dict = c1.to_dict()

        self.assertEqual(len(c1.id), 36)
        self.assertTrue(isinstance(c1, BaseModel))

        # Checking attributes types
        self.assertEqual(type(c1.id), str)
        self.assertEqual(type(c1.created_at), datetime)
        self.assertEqual(type(c1.updated_at), datetime)
        self.assertEqual(type(City.state_id), str)
        self.assertEqual(type(City.name), str)
        self.assertEqual(type(c1_dict["created_at"]), str)
        self.assertEqual(type(c1_dict["updated_at"]), str)

        self.assertLess(c1.created_at, c1.updated_at)

        # Checking __class__ attribute in __dict__ and to_dict()
        self.assertNotEqual(c1.created_at, old_updated_at)
        self.assertTrue("__class__" in c1_dict)
        self.assertTrue("__class__" not in c1.__dict__)

        # Creating a new instance using kwargs
        c2 = City(**c1_dict)

        self.assertTrue("__class__" in c2.to_dict())
        self.assertTrue("__class__" not in c2.__dict__)

        self.assertTrue(c2.to_dict()["__class__"], "BaseModel")

        # Checking datetime attributes types
        self.assertEqual(type(c2.created_at), datetime)
        self.assertEqual(type(c2.updated_at), datetime)

        # Checking if the two instances are the same object
        self.assertTrue(c1 is not c2)
        self.assertTrue(c1 != c2)

        # Checking if the two instance's attributes are equal
        self.assertEqual(c1.id, c2.id)
        self.assertEqual(c1.to_dict(), c2.to_dict())

        # Set new attribute to c2 instance
        c2.zip_code = "City 0xa7"
        self.assertNotEqual(c1.to_dict(), c2.to_dict())
        self.assertTrue("zip_code" in c2.to_dict())
        self.assertTrue("zip_code" not in c1.to_dict())

        # Tests that the each new created instance has a unique id
        c3 = City()
        self.assertNotEqual(c2.id, c3.id)
        self.assertEqual(len(c3.id), 36)

        self.assertLess(c1.created_at, c3.created_at)

    def test_save(self):
        """Tests (save) function"""
        c1 = City()
        old_updated_at = c1.updated_at

        self.assertTrue(not os.path.exists("file.json"))

        # Tests if updated_at attribute has changed after calling save() method
        c1.save()
        self.assertNotEqual(old_updated_at, c1.updated_at)

        self.assertTrue(os.path.exists("file.json"))

        with self.assertRaises(TypeError):
            c1.save(None)
        with self.assertRaises(TypeError):
            c1.save("None")
        with self.assertRaises(TypeError):
            c1.save(City())

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_str(self):
        """Tests __str__ function"""

        c1 = City()
        c1_str = f"[{c1.__class__.__name__}] ({c1.id}) {c1.__dict__}"
        self.assertEqual(c1.__str__(), c1_str)

        self.assertEqual(type(c1.__str__()), str)

        # Adding new attribute to change c1.__dict__
        c1.name = "City class"
        self.assertNotEqual(c1.__str__(), c1_str)

        with self.assertRaises(TypeError):
            c1.__str__(None)
        with self.assertRaises(TypeError):
            c1.__str__("None")

    def test_to_dict(self):
        """Tests to_dict function"""

        c1 = City()
        city_attributes = ["state_id", "name"]

        for attr in city_attributes:
            self.assertIn(attr, City.__dict__.keys())

        for attr in city_attributes:
            self.assertNotIn(attr, c1.to_dict())

        temp_dict1 = {'id': c1.id,
                      'created_at': c1.created_at.isoformat(),
                      'updated_at': c1.updated_at.isoformat(),
                      '__class__': c1.__class__.__name__
                      }

        self.assertEqual(c1.to_dict(), temp_dict1)
        self.assertNotEqual(c1.to_dict(), c1.__dict__)

        c1.name = "BaseModel class"
        self.assertNotEqual(c1.to_dict(), temp_dict1)

        temp_dict2 = {'id': c1.id,
                      'created_at': c1.created_at.isoformat(),
                      'updated_at': c1.updated_at.isoformat(),
                      '__class__': c1.__class__.__name__,
                      "name": "BaseModel class"}

        self.assertEqual(c1.to_dict(), temp_dict2)

        c1.name = "Test Man"
        self.assertIn("name", c1.to_dict())

        # Tests that created_at and updated_at from to_dict() function
        # Matching iso format
        self.assertEqual(c1.created_at,
                         datetime.fromisoformat(temp_dict1["created_at"]))

        self.assertEqual(c1.created_at,
                         datetime.strptime(temp_dict1["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

        self.assertEqual(c1.updated_at,
                         datetime.fromisoformat(temp_dict1["updated_at"]))

        self.assertEqual(c1.updated_at,
                         datetime.strptime(temp_dict1["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        with self.assertRaises(TypeError):
            c1.to_dict(None)
        with self.assertRaises(TypeError):
            c1.to_dict("None")
