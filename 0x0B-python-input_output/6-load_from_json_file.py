#!/usr/bin/python3
"""
load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from JSON file
    """

    with open(filename, mode="r", encoding="utf-8") as loadJson:
        return json.load(loadJson)
