#!/usr/bin/python3
"""
Module - 10
init method: width and height
method: def area()
str: return str
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size):
        """Initializes the class

        Args:
        - size: Length of the a side of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
