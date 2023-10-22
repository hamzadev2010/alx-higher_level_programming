#!/usr/bin/python3
"""Introduce the function"""


def add_integer(a, b=98):
    """Compute the sum of two numbers, a and b, by converting any floating-point
    values to integers before performing the addition.
    If either a or b is neither an integer nor a floating-point number,
    a TypeError will be raised.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
