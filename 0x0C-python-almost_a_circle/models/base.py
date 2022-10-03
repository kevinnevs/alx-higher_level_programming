#!/usr/bin/python3
"""
Base
"""
import json
import csv

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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string rep of list_dictionaries
        """
        if list_dictionaries is None:
           list_dictionaries = []
        return json.dumps(list_dictionaries)
