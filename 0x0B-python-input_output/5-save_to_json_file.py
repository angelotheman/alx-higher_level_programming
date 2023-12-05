#!/usr/bin/python3
"""
Module - 5
- Save JSON to file
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves JSON to file"""
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
