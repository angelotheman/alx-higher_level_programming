#!/usr/bin/python3
"""
Module: 6-square

Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0)
- Size must be an integer, otherwise raise a TypeError
  exception with the message size must be an integer
- If size is less than 0, raise a ValueError exception with
  the message size must be >= 0
- Private instance attribute: position
- Property setter: def position(self, value)
- Property getter: def position(self)
- Position must be a tuple of 2 positive integers otherwise raise a TypeError
- Public instance method: def area(self) that returns the current square area
- Public instance method: def my_print(self) that prints in stdout the square
  with the character '#'
- Setter method: def size(self, value)
- Getter method: def size(self)
"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int, optional): The size of the square,
                    Defaults to 0
            position (tuple, optional): The position of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the the size of square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The value of one side of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieves the the size of square

        Returns:
            tuple: The size of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position which is a tuple of 2 integers

        Args:
            value (tuple): The Position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

    def my_print(self):
        """Prints the square with character '#'"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
