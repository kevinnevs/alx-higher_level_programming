#!/usr/bin/python3
"""
inherits_from
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if obj isinstance of a class
    inherited (directly or indirectly) from specified class
    """

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
