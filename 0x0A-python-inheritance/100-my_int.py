#!/usr/bin/python3
"""
Module - 100
Inverted Operators
"""


class MyInt(int):
    """MyInt class that inherits from int"""

    def __eq__(self, value):
        """Inverts the equality operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts the inequality operator"""
        return super().__eq__(value)
