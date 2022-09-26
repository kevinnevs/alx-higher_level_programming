#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    Public instance area
    raises Exception message 'area() is not implemented'
    """

    def area(self):
        """
        Function not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates 'value'
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle data inherits from BseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
