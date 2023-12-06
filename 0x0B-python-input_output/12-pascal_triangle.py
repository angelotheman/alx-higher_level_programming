#!/usr/bin/python3
"""
Module - 12
- Building the Pascal triangle
"""


def pascal_triangle(n):
    """List of integers of the Pascal triangle

    Args:
    - n (int): Argument to the function

    Return:
    - list (int): List of integers that represent the triangle
    """
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
