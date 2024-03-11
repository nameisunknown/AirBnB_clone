#!/usr/bin/python3
"""This module contains TestPlace class to test Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import os


class TestPlace(unittest.TestCase):
    """This class is for testing Place class attributes and functions"""

    def test_instantiation(self):
        """Tests creating an instance of Place class"""

        p1 = Place()
        old_updated_at = p1.updated_at
        p1_dict = p1.to_dict()

        self.assertEqual(len(p1.id), 36)
        self.assertTrue(isinstance(p1, BaseModel))

        # Checking attributes types
        self.assertEqual(type(p1.id), str)
        self.assertEqual(type(p1.created_at), datetime)
        self.assertEqual(type(p1.updated_at), datetime)
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)
        self.assertEqual(type(p1_dict["created_at"]), str)
        self.assertEqual(type(p1_dict["updated_at"]), str)

        self.assertLess(p1.created_at, p1.updated_at)

        # Checking __class__ attribute in __dict__ and to_dict()
        self.assertNotEqual(p1.created_at, old_updated_at)
        self.assertTrue("__class__" in p1_dict)
        self.assertTrue("__class__" not in p1.__dict__)

        # Creating a new instance using kwargs
        p2 = Place(**p1_dict)

        self.assertTrue("__class__" in p2.to_dict())
        self.assertTrue("__class__" not in p2.__dict__)

        self.assertTrue(p2.to_dict()["__class__"], "BaseModel")

        # Checking datetime attributes types
        self.assertEqual(type(p2.created_at), datetime)
        self.assertEqual(type(p2.updated_at), datetime)

        # Checking if the two instances are the same object
        self.assertTrue(p1 is not p2)
        self.assertTrue(p1 != p2)

        # Checking if the two instance's attributes are equal
        self.assertEqual(p1.id, p2.id)
        self.assertEqual(p1.to_dict(), p2.to_dict())

        # Set new attribute to p2 instance
        p2.zip_code = "Place 0xa7"
        self.assertNotEqual(p1.to_dict(), p2.to_dict())
        self.assertTrue("zip_code" in p2.to_dict())
        self.assertTrue("zip_code" not in p1.to_dict())

        # Tests that the each new created instance has a unique id
        p3 = Place()
        self.assertNotEqual(p2.id, p3.id)
        self.assertEqual(len(p3.id), 36)

        self.assertLess(p1.created_at, p3.created_at)

    def test_save(self):
        """Tests (save) function"""
        p1 = Place()
        old_updated_at = p1.updated_at

        self.assertTrue(not os.path.exists("file.json"))

        # Tests if updated_at attribute has changed after calling save() method
        p1.save()
        self.assertNotEqual(old_updated_at, p1.updated_at)

        self.assertTrue(os.path.exists("file.json"))

        with self.assertRaises(TypeError):
            p1.save(None)
        with self.assertRaises(TypeError):
            p1.save("None")
        with self.assertRaises(TypeError):
            p1.save(Place())

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_str(self):
        """Tests __str__ function"""

        p1 = Place()
        p1_str = f"[{p1.__class__.__name__}] ({p1.id}) {p1.__dict__}"
        self.assertEqual(p1.__str__(), p1_str)

        self.assertEqual(type(p1.__str__()), str)

        # Adding new attribute to change p1.__dict__
        p1.name = "Place class"
        self.assertNotEqual(p1.__str__(), p1_str)

        with self.assertRaises(TypeError):
            p1.__str__(None)
        with self.assertRaises(TypeError):
            p1.__str__("None")

    def test_to_dict(self):
        """Tests to_dict function"""

        p1 = Place()
        place_attributes = [
            "city_id", "user_id",
            "name", "description",
            "number_rooms", "number_bathrooms",
            "max_guest", "price_by_night",
            "latitude", "longitude", "amenity_ids"
            ]

        for attr in place_attributes:
            self.assertIn(attr, Place.__dict__.keys())

        for attr in place_attributes:
            self.assertNotIn(attr, p1.to_dict())

        temp_dict1 = {'id': p1.id,
                      'created_at': p1.created_at.isoformat(),
                      'updated_at': p1.updated_at.isoformat(),
                      '__class__': p1.__class__.__name__
                      }

        self.assertEqual(p1.to_dict(), temp_dict1)
        self.assertNotEqual(p1.to_dict(), p1.__dict__)

        p1.name = "BaseModel class"
        self.assertNotEqual(p1.to_dict(), temp_dict1)

        temp_dict2 = {'id': p1.id,
                      'created_at': p1.created_at.isoformat(),
                      'updated_at': p1.updated_at.isoformat(),
                      '__class__': p1.__class__.__name__,
                      "name": "BaseModel class"}

        self.assertEqual(p1.to_dict(), temp_dict2)

        p1.name = "Test Man"
        self.assertIn("name", p1.to_dict())

        # Tests that created_at and updated_at from to_dict() function
        # Matching iso format
        self.assertEqual(p1.created_at,
                         datetime.fromisoformat(temp_dict1["created_at"]))

        self.assertEqual(p1.created_at,
                         datetime.strptime(temp_dict1["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

        self.assertEqual(p1.updated_at,
                         datetime.fromisoformat(temp_dict1["updated_at"]))

        self.assertEqual(p1.updated_at,
                         datetime.strptime(temp_dict1["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        with self.assertRaises(TypeError):
            p1.to_dict(None)
        with self.assertRaises(TypeError):
            p1.to_dict("None")
