#!/usr/bin/python3
"""
Module - 8
Class to JSON
"""
import json


def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__
