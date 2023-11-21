#!/usr/bin/python3
"""
Module: 3-square
Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0)
- Size must be an integer, otherwise raise a TypeError
  exception with the message size must be an integer
- If size is less than 0, raise a ValueError exception with
  the message size must be >= 0
- Public instance method: def area(self) that returns the current square area
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
