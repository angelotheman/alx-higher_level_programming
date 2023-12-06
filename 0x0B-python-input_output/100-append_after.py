#!/usr/bin/python3
"""
Module - 100
- Finding a string and append text afterwards
"""


def append_after(filename="", search_string="", new_string=""):
    """Append if search string is found
    
    Args:
    - filename: Name of the file
    - search_string: string to be searched
    - new_string: The new string to append
    """
    text = ""

    with open(filename, "r") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as file:
        file.write(text)
