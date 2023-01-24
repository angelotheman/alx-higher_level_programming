#!/usr/bin/python3

"""Square class
This is another square instatiation
"""

class Square:
    def __init__(self, size=0) -> int:
        """__init__
        This method initiatializes the size

        Attributes:
            size (optional): The size of the square
        
        Raises:
            TypeError: If size type is not int

            ValueError: If size is less than 0
        """

        if type(size) is not int:
            raise  TypeError('size must be an integer')
        
        if size < 0:
            raise ValueError('size must be >= 0')
        
        self.size = size
