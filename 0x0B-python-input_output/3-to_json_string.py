#!/usr/bin/python3
"""
Module - 3
- Implement JSON on objects
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of object"""
    data = json.dumps(my_obj)
    return data
