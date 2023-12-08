#!/usr/bin/python3
"""
Module - 1

- Base of all classes
- private instance: __nb_objects
"""


class Base:
    """A definition of the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class with optional id"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
