#!/usr/bin/python3
"""
Module - 1
- class: MyList
- Public instance: print_sorted
"""


class MyList(list):
    """A class inheritance of List"""

    def print_sorted(self):
        """Prints list in sorted order"""
        super().sort()
        print(self)
