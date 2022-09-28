#!/usr/bin/python3
"""
class_to_json
"""


def class_to_json(obj):
    """
    returns the dictionary description for JSON
    """

    return obj.__dict__
