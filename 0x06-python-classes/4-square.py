#!/usr/bin/python3
"""
Module: 4-square
Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0)
- Size must be an integer, otherwise raise a TypeError
  exception with the message size must be an integer
- If size is less than 0, raise a ValueError exception with
  the message size must be >= 0
- Public instance method: def area(self) that returns the current square area
- Setter method: def size(self, value)
- Getter method: def size(self)
"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int, optional): The size of the square,
                    Defaults to 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def size(self):
        """Retrieves the the size of square

        Returns:
            int: The size of the square
        """
        return self.__size

    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The value of one side of square
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
