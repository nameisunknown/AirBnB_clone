#!/usr/bin/python3

"""This module contains TestHBNBCommand class that tests HBNBCommand class"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
import models


class TestHBNBCommand(unittest.TestCase):
    """This class is for testing HBNBCommand class attributes and functions"""

    def setUp(self):
        """Setup data before each test method"""

        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Excutes data after each test method"""

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """tests public class attributes of HBNBCommand class"""

        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")
        self.assertEqual(HBNBCommand.doc_header,
                         "Documented commands (type help <topic>):")
        self.assertEqual(HBNBCommand.misc_header, "Miscellaneous help topics:")
        self.assertEqual(HBNBCommand.undoc_header, "Undocumented commands:")
        self.assertEqual(HBNBCommand.ruler, "=")

    def test_emptyline(self):
        """Tests (emptyline) function"""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit(self):
        """Tests (quit) function"""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Tests (EOF) function"""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        """Tests (help) function"""

        help_without_arg = f"{HBNBCommand.doc_header}\n" +\
            f"{HBNBCommand.ruler * len(HBNBCommand.doc_header)}\n" +\
            "EOF  all  count  create  destroy  help  quit  show  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue().strip(), help_without_arg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help do_show")
            self.assertEqual(f.getvalue().strip(), "*** No help on do_show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help do")
            self.assertEqual(f.getvalue().strip(), "*** No help on do")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_help.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_EOF.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_all.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_count.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_create.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_destroy.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_quit.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_show.__doc__.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(),
                             HBNBCommand.do_update.__doc__.strip())

    def test_create(self):
        """Tests (create) function"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("creat")
            self.assertEqual(f.getvalue().strip(), "*** Unknown syntax: creat")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Base")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        self.assertEqual(FileStorage._FileStorage__objects, {})

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        self.assertEqual(len(FileStorage._FileStorage__objects), 1)
        self.assertIn(f"BaseModel.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        self.assertEqual(len(FileStorage._FileStorage__objects), 2)
        self.assertIn(f"User.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        self.assertEqual(len(FileStorage._FileStorage__objects), 3)
        self.assertIn(f"City.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        self.assertEqual(len(FileStorage._FileStorage__objects), 4)
        self.assertIn(f"Place.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        self.assertEqual(len(FileStorage._FileStorage__objects), 5)
        self.assertIn(f"Review.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        self.assertEqual(len(FileStorage._FileStorage__objects), 6)
        self.assertIn(f"Amenity.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        self.assertEqual(len(FileStorage._FileStorage__objects), 7)
        self.assertIn(f"State.{f.getvalue().strip()}",
                      FileStorage._FileStorage__objects)

        with open("file.json", "r") as file:
            self.assertIn(f"State.{f.getvalue().strip()}", file.read())

    def test_show_no_class(self):
        """
        Tests (show) function when no class name is provided
        or invalid class name is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("showw")
            self.assertEqual(f.getvalue().strip(), "*** Unknown syntax: showw")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Base")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_BaseModel(self):
        """Tests (show) function using BaseModel class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        models.storage.reload()
        base_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {base_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"BaseModel.{base_id}"])
                )

    def test_show_User(self):
        """Tests (show) function using User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        user_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"User.{user_id}"])
                )

    def test_show_City(self):
        """Tests (show) function using City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        city_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"City.{city_id}"])
                )

    def test_show_Place(self):
        """Tests (show) function using Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        place_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {place_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Place.{place_id}"])
                )

    def test_show_Review(self):
        """Tests (show) function using Review class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        review_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {review_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Review.{review_id}"])
                )

    def test_show_Amenity(self):
        """Tests (show) function using Amenity class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        models.storage.reload()
        amenity_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Amenity.{amenity_id}"])
                )

    def test_show_State(self):
        """Tests (show) function using State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        models.storage.reload()
        state_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"State.{state_id}"])
                )

    def test_destroy_no_class(self):
        """
        Tests (destroy) function when no class name is provided
        or invalid class name is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Base")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_BaseModel(self):
        """Tests (destroy) function with BaseModel class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        models.storage.reload()
        objects = models.storage.all()
        base_id = f.getvalue().strip()
        self.assertIn(f"BaseModel.{base_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {base_id}")

        self.assertNotIn(f"BaseModel.{base_id}", objects)

    def test_destroy_User(self):
        """Tests (destroy) function with User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        models.storage.reload()
        objects = models.storage.all()
        user_id = f.getvalue().strip()
        self.assertIn(f"User.{user_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")

        self.assertNotIn(f"User.{user_id}", objects)

    def test_destroy_City(self):
        """Tests (destroy) function with City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        models.storage.reload()
        objects = models.storage.all()
        city_id = f.getvalue().strip()
        self.assertIn(f"City.{city_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {city_id}")

        self.assertNotIn(f"City.{city_id}", objects)

    def test_destroy_Place(self):
        """Tests (destroy) function with Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        models.storage.reload()
        objects = models.storage.all()
        palce_id = f.getvalue().strip()
        self.assertIn(f"Place.{palce_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {palce_id}")

        self.assertNotIn(f"Place.{palce_id}", objects)

    def test_destroy_Review(self):
        """Tests (destroy) function with Review class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        models.storage.reload()
        objects = models.storage.all()
        review_id = f.getvalue().strip()
        self.assertIn(f"Review.{review_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {review_id}")

        self.assertNotIn(f"Review.{review_id}", objects)

    def test_destroy_Amenity(self):
        """Tests (destroy) function with Amenity class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        models.storage.reload()
        objects = models.storage.all()
        amenity_id = f.getvalue().strip()
        self.assertIn(f"Amenity.{amenity_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {amenity_id}")

        self.assertNotIn(f"Amenity.{amenity_id}", objects)

    def test_destroy_State(self):
        """Tests (destroy) function with State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        models.storage.reload()
        objects = models.storage.all()
        state_id = f.getvalue().strip()
        self.assertIn(f"State.{state_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {state_id}")

        self.assertNotIn(f"State.{state_id}", objects)

    def test_all(self):
        """Tests (all) function"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Base")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), "[]")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        base_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        city_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        review_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        amenity_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        state_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 7)
            for str_obj in result_list:
                self.assertEqual(type(str_obj), str)

            self.assertIn(base_id, f.getvalue())
            self.assertIn(user_id, f.getvalue())
            self.assertIn(city_id, f.getvalue())
            self.assertIn(place_id, f.getvalue())
            self.assertIn(review_id, f.getvalue())
            self.assertIn(amenity_id, f.getvalue())
            self.assertIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertIn(base_id, result_list[0])
            self.assertIn(base_id, f.getvalue())
            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertIn(user_id, result_list[0])
            self.assertIn(user_id, f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertIn(city_id, result_list[0])
            self.assertIn(city_id, f.getvalue())
            self.assertIn("City", f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertIn(place_id, result_list[0])
            self.assertIn(place_id, f.getvalue())
            self.assertIn("Place", f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertIn(review_id, result_list[0])
            self.assertIn(review_id, f.getvalue())
            self.assertIn("Review", f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertIn(amenity_id, result_list[0])
            self.assertIn(amenity_id, f.getvalue())
            self.assertIn("Amenity", f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertIn(state_id, result_list[0])
            self.assertIn(state_id, f.getvalue())
            self.assertIn("State", f.getvalue())

    def test_update_no_class(self):
        """
        Tests (update) function when no class name is provided
        or when an invalid class name is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Base")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_BaseModel(self):
        """Tests (update) function with BaseModel class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objects = models.storage.all()
        base_id = f.getvalue().strip()
        base_obj_before_update = objects[f"BaseModel.{base_id}"]

        self.assertNotIn("name", base_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {base_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {base_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update BaseModel {base_id} name 'My first model'"
            HBNBCommand().onecmd(command)

        base_obj_after_1_update = objects[f"BaseModel.{base_id}"]
        self.assertIn("name", base_obj_after_1_update.__dict__)
        self.assertEqual(base_obj_after_1_update.name, "My first model")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update BaseModel {base_id} name 'name has changed'"
            HBNBCommand().onecmd(command)

        base_obj_after_2_update = objects[f"BaseModel.{base_id}"]
        self.assertEqual(base_obj_after_2_update.name, "name has changed")

    def test_update_User(self):
        """Tests (update) function with User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        objects = models.storage.all()
        user_id = f.getvalue().strip()
        user_obj_before_update = objects[f"User.{user_id}"]

        self.assertNotIn("name", user_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} name 'user 1'")

        user_obj_after_1_update = objects[f"User.{user_id}"]
        self.assertIn("name", user_obj_after_1_update.__dict__)
        self.assertEqual(user_obj_after_1_update.name, "user 1")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update User {user_id} name 'name has changed'"
            HBNBCommand().onecmd(command)

        user_obj_after_2_update = objects[f"User.{user_id}"]
        self.assertEqual(user_obj_after_2_update.name, "name has changed")

    def test_update_City(self):
        """Tests (update) function with City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        objects = models.storage.all()
        city_id = f.getvalue().strip()
        city_obj_before_update = objects[f"City.{city_id}"]

        self.assertNotIn("name", city_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id} name 'Cairo'")

        city_obj_after_1_update = objects[f"City.{city_id}"]
        self.assertIn("name", city_obj_after_1_update.__dict__)
        self.assertEqual(city_obj_after_1_update.name, "Cairo")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update City {city_id} name 'name has changed'"
            HBNBCommand().onecmd(command)

        city_obj_after_2_update = objects[f"City.{city_id}"]
        self.assertEqual(city_obj_after_2_update.name, "name has changed")

    def test_update_Place(self):
        """Tests (update) function with Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        objects = models.storage.all()
        place_id = f.getvalue().strip()
        place_obj_before_update = objects[f"Place.{place_id}"]

        self.assertNotIn("name", place_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} name 'Cairo'")

        place_obj_after_1_update = objects[f"Place.{place_id}"]
        self.assertIn("name", place_obj_after_1_update.__dict__)
        self.assertEqual(place_obj_after_1_update.name, "Cairo")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update Place {place_id} name 'name has changed'"
            HBNBCommand().onecmd(command)

        place_obj_after_2_update = objects[f"Place.{place_id}"]
        self.assertEqual(place_obj_after_2_update.name, "name has changed")

    def test_update_Review(self):
        """Tests (update) function with Review class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        objects = models.storage.all()
        review_id = f.getvalue().strip()
        review_obj_before_update = objects[f"Review.{review_id}"]

        self.assertNotIn("rate", review_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id} rate")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id} rate 5")

        review_obj_after_1_update = objects[f"Review.{review_id}"]
        self.assertIn("rate", review_obj_after_1_update.__dict__)
        self.assertEqual(review_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update Review {review_id} rate 'rate has changed'"
            HBNBCommand().onecmd(command)

        review_obj_after_2_update = objects[f"Review.{review_id}"]
        self.assertEqual(review_obj_after_2_update.rate, "rate has changed")

    def test_update_Amenity(self):
        """Tests (update) function with Amenity class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        objects = models.storage.all()
        amenity_id = f.getvalue().strip()
        amenity_obj_before_update = objects[f"Amenity.{amenity_id}"]

        self.assertNotIn("rate", amenity_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id} rate")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id} rate 5")

        amenity_obj_after_1_update = objects[f"Amenity.{amenity_id}"]
        self.assertIn("rate", amenity_obj_after_1_update.__dict__)
        self.assertEqual(amenity_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update Amenity {amenity_id} rate 'rate has changed'"
            HBNBCommand().onecmd(command)

        amenity_obj_after_2_update = objects[f"Amenity.{amenity_id}"]
        self.assertEqual(amenity_obj_after_2_update.rate, "rate has changed")

    def test_update_State(self):
        """Tests (update) function with State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State 123456")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        objects = models.storage.all()
        state_id = f.getvalue().strip()
        state_obj_before_update = objects[f"State.{state_id}"]

        self.assertNotIn("rate", state_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id} rate")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id} rate 5")

        state_obj_after_1_update = objects[f"State.{state_id}"]
        self.assertIn("rate", state_obj_after_1_update.__dict__)
        self.assertEqual(state_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"update State {state_id} rate 'rate has changed'"
            HBNBCommand().onecmd(command)

        state_obj_after_2_update = objects[f"State.{state_id}"]
        self.assertEqual(state_obj_after_2_update.rate, "rate has changed")

    def test_update_attr_type(self):
        """
        Tests casting attribute value to match the original attirbute type
        if the attribute already exists in the object
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create Place")

        place_id = f.getvalue().strip()
        objects = models.storage.all()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} number_rooms 7")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["number_rooms"], 7)
        self.assertEqual(type(place_obj.__dict__["number_rooms"]), int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} longitude 4.4")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["longitude"], 4.4)
        self.assertEqual(type(place_obj.__dict__["longitude"]), float)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} city_id 1")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["city_id"], "1")
        self.assertEqual(type(place_obj.__dict__["city_id"]), str)

    def test_update_attr_type_with_dict(self):
        """
        Tests casting attribute value to match the original attirbute type
        if the attribute already exists in the object using dictionary
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create Place")

        place_id = f.getvalue().strip()
        objects = models.storage.all()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} " +
                                 "{'longitude': '10.15'}")

        place_obj = objects[f"Place.{place_id}"]
        self.assertEqual(place_obj.__dict__["longitude"], 10.15)
        self.assertEqual(type(place_obj.__dict__["longitude"]), float)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} " +
                                 "{'max_guest': 10}")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["max_guest"], 10)
        self.assertEqual(type(place_obj.__dict__["max_guest"]), int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} " +
                                 "{'city_id': 4}")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["city_id"], "4")
        self.assertEqual(type(place_obj.__dict__["city_id"]), str)

    def test_count_BaseModel(self):
        """Tests (count) function with BaseModel class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Base"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count BaseModel"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count BaseModel"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count BaseModel"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_User(self):
        """Tests (count) function with User class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_City(self):
        """Tests (count) function with City class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count City"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count City"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count City"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_Place(self):
        """Tests (count) function with Place class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Place"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Place"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Place"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_Review(self):
        """Tests (count) function with Review class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Review"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Review"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Review"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_Amenity(self):
        """Tests (count) function with Amenity class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Amenity"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Amenity"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Amenity"))
            self.assertEqual("2", f.getvalue().strip())

    def test_count_State(self):
        """Tests (count) function with State class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count State"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count State"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count State"))
            self.assertEqual("2", f.getvalue().strip())

    def test_defautlt_show_no_class(self):
        """
        Tests (default) function with (show) function
        when no class name is provided or invalid class name is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("showw()")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: showw()")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: BaseModel.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: User.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: City.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Place.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Review.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Amenity.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: State.show")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Base.show()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_default_show_BaseModel(self):
        """
        Tests (default) function
        with (show) function using BaseModel class
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        models.storage.reload()
        base_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({base_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"BaseModel.{base_id}"])
                )

    def test_default_show_User(self):
        """Tests (default) function with (show) function using User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        user_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({user_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"User.{user_id}"])
                )

    def test_show_City(self):
        """Tests (default) function with (show) function using City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        city_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({city_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"City.{city_id}"])
                )

    def test_default_show_Place(self):
        """Tests (default) function with (show) function using Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        place_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({place_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Place.{place_id}"])
                )

    def test_default_show_Review(self):
        """Tests (default) function with (show) function using Review class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        review_id = f.getvalue().strip()

        models.storage.reload()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({review_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Review.{review_id}"])
                )

    def test_default_show_Amenity(self):
        """Tests (default) function (show) function using Amenity class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        models.storage.reload()
        amenity_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({amenity_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"Amenity.{amenity_id}"])
                )

    def test_default_show_State(self):
        """Tests (default) function with (show) function using State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show(12345)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        models.storage.reload()
        state_id = f.getvalue().strip()
        objects = models.storage.all()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({state_id})")
            self.assertEqual(
                f.getvalue().strip(),
                str(objects[f"State.{state_id}"])
                )

    def test_default_destroy_no_class(self):
        """
        Tests (default) function with (destroy) function
        when no class name is provided or invalid class name is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy()")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Base.destroy()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: BaseModel.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: User.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: City.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Place.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Review.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Amenity.destroy")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: State.destroy")

    def test_default_destroy_BaseModel(self):
        """
        Tests (default) functions
        with (destroy) function with BaseModel class
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        models.storage.reload()
        objects = models.storage.all()
        base_id = f.getvalue().strip()
        self.assertIn(f"BaseModel.{base_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({base_id})")

        self.assertNotIn(f"BaseModel.{base_id}", objects)

    def test_default_destroy_User(self):
        """Tests (default) function with (destroy) function with User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        models.storage.reload()
        objects = models.storage.all()
        user_id = f.getvalue().strip()
        self.assertIn(f"User.{user_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({user_id})")

        self.assertNotIn(f"User.{user_id}", objects)

    def test_default_destroy_City(self):
        """Tests (default) function with (destroy) function with City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        models.storage.reload()
        objects = models.storage.all()
        city_id = f.getvalue().strip()
        self.assertIn(f"City.{city_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({city_id})")

        self.assertNotIn(f"City.{city_id}", objects)

    def test_default_destroy_Place(self):
        """Tests (default) function with (destroy) function with Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        models.storage.reload()
        objects = models.storage.all()
        palce_id = f.getvalue().strip()
        self.assertIn(f"Place.{palce_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({palce_id})")

        self.assertNotIn(f"Place.{palce_id}", objects)

    def test_default_destroy_Review(self):
        """
        Tests (default) function
        with (destroy) function with Review class
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        models.storage.reload()
        objects = models.storage.all()
        review_id = f.getvalue().strip()
        self.assertIn(f"Review.{review_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({review_id})")

        self.assertNotIn(f"Review.{review_id}", objects)

    def test_default_destroy_Amenity(self):
        """
        Tests (default) function
        with (destroy) function with Amenity class
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        models.storage.reload()
        objects = models.storage.all()
        amenity_id = f.getvalue().strip()
        self.assertIn(f"Amenity.{amenity_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({amenity_id})")

        self.assertNotIn(f"Amenity.{amenity_id}", objects)

    def test_default_destroy_State(self):
        """Tests (default) function with (destroy) function with State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        models.storage.reload()
        objects = models.storage.all()
        state_id = f.getvalue().strip()
        self.assertIn(f"State.{state_id}", objects)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({state_id})")

        self.assertNotIn(f"State.{state_id}", objects)

    def test_default_all(self):
        """Tests (defualt) function with (all) function"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Base.all()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
            self.assertEqual(f.getvalue().strip(), "[]")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        base_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        city_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        review_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        amenity_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        state_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 7)
            for str_obj in result_list:
                self.assertEqual(type(str_obj), str)

            self.assertIn(base_id, f.getvalue())
            self.assertIn(user_id, f.getvalue())
            self.assertIn(city_id, f.getvalue())
            self.assertIn(place_id, f.getvalue())
            self.assertIn(review_id, f.getvalue())
            self.assertIn(amenity_id, f.getvalue())
            self.assertIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertIn(base_id, result_list[0])
            self.assertIn(base_id, f.getvalue())
            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertIn(user_id, result_list[0])
            self.assertIn(user_id, f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertIn(city_id, result_list[0])
            self.assertIn(city_id, f.getvalue())
            self.assertIn("City", f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertIn(place_id, result_list[0])
            self.assertIn(place_id, f.getvalue())
            self.assertIn("Place", f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertIn(review_id, result_list[0])
            self.assertIn(review_id, f.getvalue())
            self.assertIn("Review", f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertIn(amenity_id, result_list[0])
            self.assertIn(amenity_id, f.getvalue())
            self.assertIn("Amenity", f.getvalue())
            self.assertNotIn(state_id, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            result_list = eval(f.getvalue())
            self.assertEqual(len(result_list), 1)
            self.assertEqual(type(result_list[0]), str)

            self.assertNotIn(base_id, f.getvalue())
            self.assertNotIn(user_id, f.getvalue())
            self.assertNotIn(city_id, f.getvalue())
            self.assertNotIn(place_id, f.getvalue())
            self.assertNotIn(review_id, f.getvalue())
            self.assertNotIn(amenity_id, f.getvalue())
            self.assertIn(state_id, result_list[0])
            self.assertIn(state_id, f.getvalue())
            self.assertIn("State", f.getvalue())

    def test_default_update_no_class(self):
        """
        Tests (default) function with (update) function
        when no class name is provided or when an invalid class is provided
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Base.update()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_default_update_BaseModel(self):
        """
        Tests (default) function
        with (update) function with BaseModel class
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        objects = models.storage.all()
        base_id = f.getvalue().strip()
        base_obj_before_update = objects[f"BaseModel.{base_id}"]

        self.assertNotIn("name", base_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({base_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({base_id}, name)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"BaseModel.update({base_id}, name, 'My first model')"
            HBNBCommand().onecmd(command)

        base_obj_after_1_update = objects[f"BaseModel.{base_id}"]
        self.assertIn("name", base_obj_after_1_update.__dict__)
        self.assertEqual(base_obj_after_1_update.name, "My first model")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"BaseModel.update({base_id}, name, 'name has changed')"
            HBNBCommand().onecmd(command)

        base_obj_after_2_update = objects[f"BaseModel.{base_id}"]
        self.assertEqual(base_obj_after_2_update.name, "name has changed")

    def test_default_update_User(self):
        """Tests (default) function with (update) function with User class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: User.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        objects = models.storage.all()
        user_id = f.getvalue().strip()
        user_obj_before_update = objects[f"User.{user_id}"]

        self.assertNotIn("name", user_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({user_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({user_id}, name)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({user_id}, name, 'user 1')")

        user_obj_after_1_update = objects[f"User.{user_id}"]
        self.assertIn("name", user_obj_after_1_update.__dict__)
        self.assertEqual(user_obj_after_1_update.name, "user 1")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"User.update({user_id}, name, 'name has changed')"
            HBNBCommand().onecmd(command)

        user_obj_after_2_update = objects[f"User.{user_id}"]
        self.assertEqual(user_obj_after_2_update.name, "name has changed")

    def test_default_update_City(self):
        """Tests (default) function with (update) function with City class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: City.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        objects = models.storage.all()
        city_id = f.getvalue().strip()
        city_obj_before_update = objects[f"City.{city_id}"]

        self.assertNotIn("name", city_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({city_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({city_id}, name)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({city_id}, name, 'Cairo')")

        city_obj_after_1_update = objects[f"City.{city_id}"]
        self.assertIn("name", city_obj_after_1_update.__dict__)
        self.assertEqual(city_obj_after_1_update.name, "Cairo")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"City.update({city_id}, name, 'name has changed')"
            HBNBCommand().onecmd(command)

        city_obj_after_2_update = objects[f"City.{city_id}"]
        self.assertEqual(city_obj_after_2_update.name, "name has changed")

    def test_default_update_Place(self):
        """Tests (default) function with (update) function with Place class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Place.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        objects = models.storage.all()
        place_id = f.getvalue().strip()
        place_obj_before_update = objects[f"Place.{place_id}"]

        self.assertNotIn("name", place_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, name)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, name, 'Cairo')")

        place_obj_after_1_update = objects[f"Place.{place_id}"]
        self.assertIn("name", place_obj_after_1_update.__dict__)
        self.assertEqual(place_obj_after_1_update.name, "Cairo")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"Place.update({place_id}, name, 'name has changed')"
            HBNBCommand().onecmd(command)

        place_obj_after_2_update = objects[f"Place.{place_id}"]
        self.assertEqual(place_obj_after_2_update.name, "name has changed")

    def test_default_update_Review(self):
        """Tests (default) function with (update) function with Review class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Review.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        objects = models.storage.all()
        review_id = f.getvalue().strip()
        review_obj_before_update = objects[f"Review.{review_id}"]

        self.assertNotIn("rate", review_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({review_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({review_id}, rate)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({review_id}, rate, 5)")

        review_obj_after_1_update = objects[f"Review.{review_id}"]
        self.assertIn("rate", review_obj_after_1_update.__dict__)
        self.assertEqual(review_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"Review.update({review_id}, rate, 'rate has changed')"
            HBNBCommand().onecmd(command)

        review_obj_after_2_update = objects[f"Review.{review_id}"]
        self.assertEqual(review_obj_after_2_update.rate, "rate has changed")

    def test_default_update_Amenity(self):
        """Test (default) function with (update) function with Amenity class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: Amenity.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        objects = models.storage.all()
        amenity_id = f.getvalue().strip()
        amenity_obj_before_update = objects[f"Amenity.{amenity_id}"]

        self.assertNotIn("rate", amenity_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({amenity_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({amenity_id}, rate)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({amenity_id}, rate, 5)")

        amenity_obj_after_1_update = objects[f"Amenity.{amenity_id}"]
        self.assertIn("rate", amenity_obj_after_1_update.__dict__)
        self.assertEqual(amenity_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"Amenity.update({amenity_id}, rate, 'rate has changed')"
            HBNBCommand().onecmd(command)

        amenity_obj_after_2_update = objects[f"Amenity.{amenity_id}"]
        self.assertEqual(amenity_obj_after_2_update.rate, "rate has changed")

    def test_default_update_State(self):
        """Tests (defualt) function with (update) function with State class"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: State.update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update(123456)")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        objects = models.storage.all()
        state_id = f.getvalue().strip()
        state_obj_before_update = objects[f"State.{state_id}"]

        self.assertNotIn("rate", state_obj_before_update.__dict__)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({state_id})")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({state_id}, rate)")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({state_id}, rate, 5)")

        state_obj_after_1_update = objects[f"State.{state_id}"]
        self.assertIn("rate", state_obj_after_1_update.__dict__)
        self.assertEqual(state_obj_after_1_update.rate, "5")

        with patch('sys.stdout', new=StringIO()) as f:
            command = f"State.update({state_id}, rate, 'rate has changed')"
            HBNBCommand().onecmd(command)

        state_obj_after_2_update = objects[f"State.{state_id}"]
        self.assertEqual(state_obj_after_2_update.rate, "rate has changed")

    def test_default_update_attr_type(self):
        """
        Tests (default) function with (update) function to check that update()
        casts attribute value to match the original attirbute type
        if the attribute already exists in the object when updating an object
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create Place")

        place_id = f.getvalue().strip()
        objects = models.storage.all()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, number_rooms, 7)")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["number_rooms"], 7)
        self.assertEqual(type(place_obj.__dict__["number_rooms"]), int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, longitude, 4.4)")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["longitude"], 4.4)
        self.assertEqual(type(place_obj.__dict__["longitude"]), float)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, city_id, 1)")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["city_id"], "1")
        self.assertEqual(type(place_obj.__dict__["city_id"]), str)

    def test_default_update_attr_type_with_dict(self):
        """
        Tests (default) function with (update) function to check that update()
        casts attribute value to match the original attirbute type
        if the attribute already exists in the object when updating an object
        with sending the attribbute name and value as a dictionary
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create Place")

        place_id = f.getvalue().strip()
        objects = models.storage.all()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, " +
                                 "{'longitude': '10.15'})")

        place_obj = objects[f"Place.{place_id}"]
        self.assertEqual(place_obj.__dict__["longitude"], 10.15)
        self.assertEqual(type(place_obj.__dict__["longitude"]), float)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, " +
                                 "{'max_guest': 10})")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["max_guest"], 10)
        self.assertEqual(type(place_obj.__dict__["max_guest"]), int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({place_id}, " +
                                 "{'city_id': 4})")

        place_obj = objects[f"Place.{place_id}"]

        self.assertEqual(place_obj.__dict__["city_id"], "4")
        self.assertEqual(type(place_obj.__dict__["city_id"]), str)

    def test_default_count_BaseModel(self):
        """
        Tests (default) function
        with (count) function with BaseModel class
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Base.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_User(self):
        """Tests (default) function with (count) function with User class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_City(self):
        """Tests (default) function with (count) function with City class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_Place(self):
        """Tests (defualt) function with (count) function with Place class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_Review(self):
        """Tests (default) function with (count) function with Review class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_Amenity(self):
        """Tests (default) function with (count) function with Amenity class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("2", f.getvalue().strip())

    def test_default_count_State(self):
        """Tests (default) function with (count) function with State class"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("0", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("2", f.getvalue().strip())
