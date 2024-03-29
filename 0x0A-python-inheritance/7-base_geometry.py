#!/usr/bin/python3
"""
Module - 7
Public instance: def area
Public instance: def integer_validator
"""


class BaseGeometry:
    """The BaseGeometry Class"""

    def area(self):
        """Simply to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value

        Args:
        - name (str): Name
        - value: Value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
