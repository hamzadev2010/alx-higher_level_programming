#!/usr/bin/python3
"""Introduce the function"""


def print_square(size):
    """Arguments:

size (int): The height and width of the square.
Raises:

TypeError: If size is not an integer.
ValueError: If size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
