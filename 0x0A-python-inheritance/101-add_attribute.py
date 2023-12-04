#!/usr/bin/python3
"""
Module - 101
Add attribute to the object
"""


def add_attribute(obj, attribute, value):
    """Adds new attribute to an object if possible"""
    if '__dict__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
