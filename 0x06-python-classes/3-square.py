#!/usr/bin/python3
"""
empty
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """
    def __init__(self, size=0):
        """
        private instance attribute
        paramts
        size : integer or TypError
        if size less than zero, raise value error
        """
        self.__size = size
        try:
            assert type(size) == int
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        return square 
        """
        return self.__size ** 2
