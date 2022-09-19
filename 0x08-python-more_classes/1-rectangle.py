#!/usr/bin/python3
"""
Rectangle class that defines a rectangle
"""


class Rectangle:
    """
    Rectangle functions and data
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.width = width
        self.height = height

    """
    Rectangles width
    Width must be an integer
    Width is less than 0
    """
    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    Rectangles height
    Height must be an integer
    Height is greater than 0
    """
    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
