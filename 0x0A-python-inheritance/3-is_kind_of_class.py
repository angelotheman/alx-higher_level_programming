#!/usr/bin/python3
"""
Module - 3
-Subclasses
-IsInstance types
"""


def is_kind_of_class(obj, a_class):
    """Check for instances of the obj to the class type"""
    return isinstance(obj, a_class) or type(obj) == a_class
