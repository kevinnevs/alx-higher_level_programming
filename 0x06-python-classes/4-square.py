#!/usr/bin/python3
"""
Defines class square with private size and public area

Can access and update size
"""


class Square:
    """
    class Square definition

    Args:
       size (int): size of a side in square

    Functions:
    __init__(self, size)
    size(self)
    size(self, value)
    area(self)
    """

    def __init__(self, size=0):
        """
        Intitializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.__size = size

    # Property
    @property
    def size(self):
        """
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of a square

        Returns :
            area
        """

        return self.__size ** 2
