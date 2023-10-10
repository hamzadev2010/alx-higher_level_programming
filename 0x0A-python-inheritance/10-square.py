#!/usr/bin/python3
"""Specifies a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Introduce the  rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the new Rectangle.
            width int: The width of the new Rectangle.
            height int: The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() thet represent Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
