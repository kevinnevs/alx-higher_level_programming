#!/usr/bin/python3
"""
from_json_string
"""
import json


def from_json_string(my_str):
    """
    returns an object (python data structures)
    represented by JSON string
    """

    return json.loads(my_str)
