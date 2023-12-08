#!/usr/bin/python3
"""
Module - Square class
- Inherits from the Rectangle class
- Constructor: size, x, y, id
- __str__: Returns a stringified class
"""


class Square(Rectangle):
    """Square inherits from the Rectangle class

    Private instance attributes:
    - size: Length of one side of the square
    - All others from the Rectangle except width and height
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class

        Args:
        - size (int): The size of one side of the square
        - x (int): Horizontal coordinates
        - y (int): Vertical coordinates
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method to represent the class"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}""
