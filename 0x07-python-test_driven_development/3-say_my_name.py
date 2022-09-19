#!/usr/bin/python3
"""
say_my_name prints "My name is <first name> <last name>"
last name is defaulted to an empty string
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be a string
    checks if first_name is string
    checks if last_name is string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
