i#!/usr/bin/python3
"""This module contains TestReview class to test Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import os


class TestReview(unittest.TestCase):
    """This class is for testing Review class attributes and functions"""

    def test_instantiation(self):
        """Tests creating an instance of Review class"""

        r1 = Review()
        old_updated_at = r1.updated_at
        r1_dict = r1.to_dict()

        self.assertEqual(len(r1.id), 36)
        self.assertTrue(isinstance(r1, BaseModel))

        # Checking attributes types
        self.assertEqual(type(r1.id), str)
        self.assertEqual(type(r1.created_at), datetime)
        self.assertEqual(type(r1.updated_at), datetime)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.text), str)
        self.assertEqual(type(r1_dict["created_at"]), str)
        self.assertEqual(type(r1_dict["updated_at"]), str)

        self.assertLess(r1.created_at, r1.updated_at)

        # Checking __class__ attribute in __dict__ and to_dict()
        self.assertNotEqual(r1.created_at, old_updated_at)
        self.assertTrue("__class__" in r1_dict)
        self.assertTrue("__class__" not in r1.__dict__)

        # Creating a new instance using kwargs
        r2 = Review(**r1_dict)

        self.assertTrue("__class__" in r2.to_dict())
        self.assertTrue("__class__" not in r2.__dict__)

        self.assertTrue(r2.to_dict()["__class__"], "BaseModel")

        # Checking datetime attributes types
        self.assertEqual(type(r2.created_at), datetime)
        self.assertEqual(type(r2.updated_at), datetime)

        # Checking if the two instances are the same object
        self.assertTrue(r1 is not r2)
        self.assertTrue(r1 != r2)

        # Checking if the two instance's attributes are equal
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.to_dict(), r2.to_dict())

        # Set new attribute to r2 instance
        r2.zip_code = "Review 0xa7"
        self.assertNotEqual(r1.to_dict(), r2.to_dict())
        self.assertTrue("zip_code" in r2.to_dict())
        self.assertTrue("zip_code" not in r1.to_dict())

        # Tests that the each new created instance has a unique id
        r3 = Review()
        self.assertNotEqual(r2.id, r3.id)
        self.assertEqual(len(r3.id), 36)

        self.assertLess(r1.created_at, r3.created_at)

    def test_save(self):
        """Tests (save) function"""
        r1 = Review()
        old_updated_at = r1.updated_at

        self.assertTrue(not os.path.exists("file.json"))

        # Tests if updated_at attribute has changed after calling save() method
        r1.save()
        self.assertNotEqual(old_updated_at, r1.updated_at)

        self.assertTrue(os.path.exists("file.json"))

        with self.assertRaises(TypeError):
            r1.save(None)
        with self.assertRaises(TypeError):
            r1.save("None")
        with self.assertRaises(TypeError):
            r1.save(Review())

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_str(self):
        """Tests __str__ function"""

        r1 = Review()
        r1_str = f"[{r1.__class__.__name__}] ({r1.id}) {r1.__dict__}"
        self.assertEqual(r1.__str__(), r1_str)

        self.assertEqual(type(r1.__str__()), str)

        # Adding new attribute to change r1.__dict__
        r1.name = "Review class"
        self.assertNotEqual(r1.__str__(), r1_str)

        with self.assertRaises(TypeError):
            r1.__str__(None)
        with self.assertRaises(TypeError):
            r1.__str__("None")

    def test_to_dict(self):
        """Tests to_dict function"""

        r1 = Review()
        review_attributes = ["place_id", "user_id", "text"]

        for attr in review_attributes:
            self.assertIn(attr, Review.__dict__.keys())

        for attr in review_attributes:
            self.assertNotIn(attr, r1.to_dict())

        temp_dict1 = {'id': r1.id,
                      'created_at': r1.created_at.isoformat(),
                      'updated_at': r1.updated_at.isoformat(),
                      '__class__': r1.__class__.__name__
                      }

        self.assertEqual(r1.to_dict(), temp_dict1)
        self.assertNotEqual(r1.to_dict(), r1.__dict__)

        r1.name = "BaseModel class"
        self.assertNotEqual(r1.to_dict(), temp_dict1)

        temp_dict2 = {'id': r1.id,
                      'created_at': r1.created_at.isoformat(),
                      'updated_at': r1.updated_at.isoformat(),
                      '__class__': r1.__class__.__name__,
                      "name": "BaseModel class"}

        self.assertEqual(r1.to_dict(), temp_dict2)

        r1.name = "Test Man"
        self.assertIn("name", r1.to_dict())

        # Tests that created_at and updated_at from to_dict() function
        # Matching iso format
        self.assertEqual(r1.created_at,
                         datetime.fromisoformat(temp_dict1["created_at"]))

        self.assertEqual(r1.created_at,
                         datetime.strptime(temp_dict1["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

        self.assertEqual(r1.updated_at,
                         datetime.fromisoformat(temp_dict1["updated_at"]))

        self.assertEqual(r1.updated_at,
                         datetime.strptime(temp_dict1["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        with self.assertRaises(TypeError):
            r1.to_dict(None)
        with self.assertRaises(TypeError):
            r1.to_dict("None")
