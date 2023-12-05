#!/usr/bin/python3
"""
Module - 0
- One read function
"""


def read_file(filename=""):
    """Reads file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as text:
        content = text.read()
        print(content, end='')
