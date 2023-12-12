#!/usr/bin/python3
"""
Module - Square class
- Inherits from the Rectangle class
- Constructor: size, x, y, id
- __str__: Returns a stringified class
- Getters and setters for all inheriting from the Rectangle
- Public methods
    - Update methods with little tweak
    - Dictionary methods
"""
Rectangle = __import__("Rectangle").Rectangle


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
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Assigns with and height to the same value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes using *args and **kwargs for Square"""
        if args:
            attributes = ["id", "size", "x", "y"]

            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of the square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
