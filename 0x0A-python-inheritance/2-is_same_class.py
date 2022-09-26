#!/usr/bin/python3
"""
is_same_class - funct that returns true or false
if obj is exactly an instance of spec class
"""


def is_same_class(obj, a_class):
    """
    Type obj
    returns true or false
    """

    if type(obj) is a_class:
        return True
    else:
        return False
