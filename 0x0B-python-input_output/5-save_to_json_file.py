#!/usr/bin/python3
"""
save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON
    """

    with open(filename, mode="w", encoding="utf-8") as writeJsonFile:
        json.dump(my_obj, writeJsonFile)
