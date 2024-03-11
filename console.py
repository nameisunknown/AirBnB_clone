#!/usr/bin/python3

"""This module contains HBNBCommand class"""

import cmd
import models
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from shlex import split
import re


class HBNBCommand(cmd.Cmd):
    """
    Tests the functionality of the project through terminal
    using cmd.Cmd class as super class
    """

    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    def do_EOF(self, line):
        """Recieves the end of a file marker and returns True"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Returns an empty string if no command is entered"""
        pass

    def default(self, line: str) -> None:
        """
        Called on an input line when the command prefix is not recognized
        in this case it will re directr the line to the write method when
        a certain command format is passed. Ex: User.all()

        Args:
            line (str): Is the line to look through
        """

        commands = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
            }
        splitted_line = line.split(".", 1)

        class_name = splitted_line[0]

        if len(splitted_line) > 1:
            command = splitted_line[1].split("(")[0]
            if command in commands:
                match = re.search(r"(\(.*\))", splitted_line[1])
                if match is not None:
                    arg = match.group()[1:-1]
                    new_line = f"{class_name} {arg}"
                    return commands[command](new_line.strip())

        print(f"*** Unknown syntax: {line}")
        return False

    def do_create(self, argv):
        """
        Creates a new instance of a class
        saves it (to the JSON file) and prints the id. Ex: ($ create BaseModel)

        Args:
            argv (str): The arguments passed to the command
        """

        arguments = split(argv)
        if not argv:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arguments[0] + "()")
            models.storage.save()
            print(new_obj.id)

    def do_show(self, argv):
        """
        Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

        Args:
            argv (str): The arguments passed to the command
        """

        models.storage.reload()
        all_class_objs = models.storage.all()
        if not argv:
            print("** class name missing **")
        else:
            arguments = split(argv)

            if arguments[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif arguments[0] in HBNBCommand.__classes and len(arguments) < 2:
                print("** instance id missing **")
            elif f"{arguments[0]}.{arguments[1]}" not in all_class_objs.keys():
                print("** no instance found **")
            else:
                obj_key = f"{arguments[0]}.{arguments[1]}"
                print(all_class_objs[obj_key])

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.

        Args:
            args (str): The arguments passed to the command
        """

        obj_list = []
        models.storage.reload()
        all_class_objs = models.storage.all()

        class_name = ""

        if args:
            args = split(args)
            class_name = args[0]

        if not class_name:
            for key, value in all_class_objs.items():
                obj_list.append(str(value))
            print(obj_list)
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:  # a name of a class that exists is given
            for key, value in all_class_objs.items():
                if class_name in key:
                    obj_list.append(str(value))
            print(obj_list)

    def do_destroy(self, argv):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.

        Args:
            argv (str): The arguments passed to the command
        """

        arguments = split(argv)
        models.storage.reload()
        all_class_objs = models.storage.all()

        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif f"{arguments[0]}.{arguments[1]}" not in all_class_objs.keys():
            print("** no instance found **")
        else:
            del all_class_objs[f"{arguments[0]}.{arguments[1]}"]
            models.storage.save()

    def do_update(self, argv):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com.
        Usage: update <class name> <id> <attribute name> '<attribute value>'

        Args:
            argv (str): The arguments passed to the command
        """
        # shlex function to take care of "" when taking argv
        arguments = self.check_for_dict(argv)
        argv_num = len(arguments)
        models.storage.reload()
        all_objs = models.storage.all()

        if argv_num < 1:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif argv_num < 2:
            print("** instance id missing **")
        elif f"{arguments[0]}.{arguments[1]}" not in all_objs.keys():
            print("** no instance found **")
        elif argv_num < 3:
            print("** attribute name missing **")
        elif argv_num < 4:

            if type(arguments[2]) is dict:
                obj_key = f"{arguments[0]}.{arguments[1]}"
                obj = all_objs[obj_key]

                for key, value in arguments[2].items():
                    if key in obj.__class__.__dict__:
                        value_type = type(obj.__class__.__dict__[key])
                        value = value_type(value)
                    obj.__dict__[key] = value
                models.storage.save()
                return False

            print("** value missing **")
        else:
            obj = all_objs[f"{arguments[0]}.{arguments[1]}"]
            attr_name = arguments[2]
            attr_value = arguments[3]

            if arguments[2] in obj.__class__.__dict__:
                value_type = type(obj.__class__.__dict__[attr_name])
                attr_value = value_type(attr_value)

            obj.__dict__[arguments[2]] = attr_value
            models.storage.save()

    def do_count(self, args):
        """
        Retrieves the number of instances of a class: <class name>.count().

        Args:
            args (str): The arguments passed to the command
        """
        count = 0
        cls_name = ""

        if args:
            args = split(args)
            cls_name = args[0]

        models.storage.reload()
        objects = models.storage.all()
        for value in objects.values():
            if cls_name == value.__class__.__name__:
                count += 1

        print(count)

    def check_for_dict(self, line):
        """
        Checks if the line has a dict representation and return a list of args
        Args:
            line (str): Is the line to check
        """

        args = []

        dictionary = re.search(r"(\{.*\})", line)

        if dictionary:
            line = line[:dictionary.span()[0]]
            line = line.replace(",", "")
            args = [arg for arg in split(line)]
            args.append(eval(dictionary.group()))
            return args
        else:
            line = line.replace(",", "")
            return [arg for arg in split(line)]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
