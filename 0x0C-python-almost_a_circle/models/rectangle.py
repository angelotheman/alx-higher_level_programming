#!/usr/bin/python3
"""
- Module inherits from Base
- Private instance attributes: width, height, x, y
- Getter/Setter for each
- Initialization for each
- Checks for validation of all attributes
- Public instance:
    - def Area(self): Area of rectangle
    - def display(self): Display area as # with x and y offsets
    - def update(self, *args): Assigns argument to each attribute
    - def to_dictionary(self): Returns the dictionary represenation
- __str__ method to display string version of class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from the Base class

    Private instance attributes:
    - __width: Width of the rectangle
    - __height: Height of the rectangle
    - __x: x-coordinate of the rectangle's position
    - __y: y-coordinate of the rectangle's position

    Each attribute has it's own getter and setter method
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle's class

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): x-coordinate of the rectangle's position
            y (int, optional): y-coordinate of the rectangle's position
            id (int, optional): Identifier of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the Rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the Rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x of the Rectangle"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y of the Rectangle"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Returns the width and height in #
        It also considers the x and y coordinates
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Assigns args to values in order"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]

            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of the object"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

    def __str__(self):
        """Returns human readable object class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
