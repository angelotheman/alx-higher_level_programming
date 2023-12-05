#!/usr/bin/python3
"""
Module - 1
- Implement a write function
"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, "x", encoding="utf-8") as f:
        f.write(text)
        return len(text)
