#!/usr/bin/python3
"""
Module - 4
- Implement JSON on objects
"""
import json


def from_json_string(my_str):
    """Returns JSON representation of object"""
    data = json.loads(my_str)
    return data
