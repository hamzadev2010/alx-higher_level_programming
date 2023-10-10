#!/usr/bin/python3
"""Specifies a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Introduce a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the new Rectangle.
            width int: width of the new Rectangle.
            height int: height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
