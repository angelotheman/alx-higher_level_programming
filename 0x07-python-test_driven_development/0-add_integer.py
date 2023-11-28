#!/usr/bin/python3
"""
Contains a function that adds two integers
"""


def add_integers(a, b=98):
    """Returns the results of two integers

        Args:
        - a: First number
        - b: Second number

        Raises:
        - TypeError: If a or b is not an integer or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
