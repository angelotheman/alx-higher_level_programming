#!/usr/bin/python3
"""
Module: 2
- Size must be an integer, otherwise raise a TypeError
  exception with the message size must be an integer
- If size is less than 0, raise a ValueError
  exception with the message size must be >= 0
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
