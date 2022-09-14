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
    __init__(self, size, position)
    size(self)
    size(self, value)
    position(self)
    position(self, value(
    area(self)
    my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Intitializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuples of two positive integers
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)

        self.__position = value

    def area(self):
        """
        Calculates the area of a square

        Returns :
            area
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints square with #'s
        """

        size = self.__size
        n1 = self.__position[1]
        ws = self.__position[0]

        if size == 0:
            print()

        for newlines in range(n1):
            print()

        for row in range(size):
            print((' ' * ws) + ('#' * size))
