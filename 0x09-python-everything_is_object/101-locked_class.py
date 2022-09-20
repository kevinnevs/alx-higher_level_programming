#!/usr/bin/python3
"""
LockedClass prevents user creating new inst attr
Except first_name attribute
"""


class LockedClass:
    """
    No class or object attributes
    Except first_name
    """
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '"
                  + attribute + "'")
