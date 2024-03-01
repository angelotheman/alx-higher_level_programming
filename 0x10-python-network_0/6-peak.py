#!/usr/bin/python3
"""
Defines a peak-finding algorithm
"""


def find_peak(list_of_integers):
    """
    Finds the highest number in a list of integers

    Args:
        list_of_integers: List (int)
    Return:
        the highest number
    """

    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        left = 0
        right = len(list_of_integers) - 1

        while left < right:
            mid = (left + right) // 2

            if list_of_integers[mid] < list_of_integers[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return list_of_integers[left]
