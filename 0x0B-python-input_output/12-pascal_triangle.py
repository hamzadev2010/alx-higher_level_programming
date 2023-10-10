#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers.
n (int): The number of lists and digits.
Returns:
A list of lists
    """
    row = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            row[n][i + 1] = sum(row[n - 1][i:i + 2])
    return row
