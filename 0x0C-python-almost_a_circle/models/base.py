#!/usr/bin/python3
"""
Base
"""
import json


class Base:
    """
    defines class Base
    Class attributes:
       __nb_objects
    Methods:
       __init_(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string rep json_string
        """
        if json_string is None:
            json_string = "[]"
        return json.load(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write JSON string rep of list_objs to a file
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instance with attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        x = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                x.append(cls.create(**instances[i]))
        except Exception:
            pass
        return x
