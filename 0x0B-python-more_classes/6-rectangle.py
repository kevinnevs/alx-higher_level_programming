#!/usr/bin/python3
"""
Rectangle class that defines a rectangle
"""


class Rectangle:
    """
    Rectangle functions and data
    """
    # Public
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        The area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        The parameter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        print() __str__ method function to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res

    def __repr__(self):
        """
        print() or eval() __repr__ method function to return
        ... Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """
        Print message for del
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
