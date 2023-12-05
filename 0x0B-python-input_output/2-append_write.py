#!/usr/bin/python3
"""
Module - 2
- Implement an append function
"""


def append_write(filename="", text=""):
    """Appends to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.append(text)
        return len(text)
