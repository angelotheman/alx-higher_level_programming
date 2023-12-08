#!/usr/bin/python3
"""
- Module inherits from Base
- Private instance attributes: width, height, x, y
- Getter/Setter for each
- Initialization for each
"""


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the Rectangle"""
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))
        elif width <= 0:
            raise ValueError("{} must be > 0".format(width))

        self.__width = width

    @property
    def height(self):
        """Returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the Rectangle"""
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height))
        elif height <= 0:
            raise ValueError("{} must be > 0".format(height))

        self.__height = height

    @property
    def x(self):
        """Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x of the Rectangle"""
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format(x))
        elif < 0:
            raise ValueError("{} must be >= 0".format(x))

        self.__x = x

    @property
    def y(self):
        """Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y of the Rectangle"""
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format(y))
        elif < 0:
            raise ValueError("{} must be >= 0".format(y))

        self.__y = y