#!/usr/bin/python3
"""intruduce a class Square."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size
