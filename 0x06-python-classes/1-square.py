#!/usr/bin/python3
"""
Module: 1
Private instance attribute: size
Instantiation with size (no type/value verification
"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
