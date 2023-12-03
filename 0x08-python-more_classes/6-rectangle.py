#!/usr/bin/python3
"""
Module - 6
Private instance: width
Setter: def width(self, value)
Getter: def width(self)
Private instance: height
Setter: def height(self, value)
Getter: def height(value)
Public instance: area, perimeter
Implement str and repr
Initialize and delete
Public attr: number_of_instances
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization with optional parameters

            Args:
                width (optional, int): the width of rectangle
                height (optional, int): the height of rectangle
        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    def __del__(self, width=0, height=0):
        """Destructor that prints message when instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        message = ""
        for _ in range(self.__height):
            message += "#" * self.__width + "\n"

        return message

    def __repr__(self):
        """Returns a string representation of the rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
