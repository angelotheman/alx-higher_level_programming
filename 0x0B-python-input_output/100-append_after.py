#!/usr/bin/python3
"""
Module - 100
- Finding a string and append text afterwards
"""


def append_after(filename="", search_string="", new_string=""):
    """Append if search string is found"""
    with open(filename, "r+") as file:
        while True:
            position = file.tell()

            line = file.readline()

            if not line:
                break

            if search_string in line:
                file.seek(position + len(line))

                file.write("{}\n".format(new_string))

                break
