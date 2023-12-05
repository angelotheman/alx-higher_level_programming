#!/usr/bin/python3
"""
Module - 8
init method: width and height
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle Class"""

    def __init__(self, width, height):
        """Initializes the class

        Args:
        - width: Width of the figure
        - height: Height of the figure
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
