#!/usr/bin/python3
"""
Module - 5
- Creates object from JSON file
"""
import json


def load_from_json_file(my_obj, filename):
    """Loads JSON from file"""
    with open(filename, "r", encoding="utf-8") as json_file:
        json.load(json_file)
