#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):    
    """
    defines class Square; inherits from class Rectangle
    Inherited Attributes:
        id
        __weight        __height
        __x             __y
    Class Attributes:
        size
    Inherted Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        size(self)       size(self, value)
        to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initiliaze
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
        Getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size must be an int
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns formatted informaton display
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
            else:
                print()

    def to_dictionary(self):
        """
        Returns a dict representation
        """

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
