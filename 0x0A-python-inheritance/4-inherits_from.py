#!/usr/bin/python3
"""
Module - 4
Subclasses
"""


def inherits_from(obj, a_class):
    """Returns True for Subclasses or False otherwise"""
    return isinstance(obj, a_class) and type(obj) is not a_class
