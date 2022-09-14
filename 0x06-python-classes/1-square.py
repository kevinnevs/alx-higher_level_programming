#!/usr/bin/python3
"""
creates a square and sets size as private attribute
"""


class Square:
    """
    class Square definition
    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initiliazes square

        Attributes:
            size: size of a side of a square
        """
        self.__size = size
