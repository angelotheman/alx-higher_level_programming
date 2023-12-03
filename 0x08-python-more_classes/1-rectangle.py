#!/usr/bin/python3
"""
Module - 1
Private instance: width
Setter: def width(self, value)
Getter: def width(self)
Private instance: height
Setter: def height(self, value)
Getter: def height(value)
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialization with optional parameters

            Args:
                width (optional, int): the width of rectangle
                height (optional, int): the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set's the width of the rectangle

        Args:
            Value: The value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set's the height of the rectangle

            Args:
                Value: The value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
