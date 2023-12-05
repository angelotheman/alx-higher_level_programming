#!/usr/bin/python3
"""
Module - 6
- Creates object from JSON file
"""
import json


def load_from_json_file(filename):
    """Loads JSON from file"""
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data
