#!/usr/bin/python3
"""Module 7-base_geometry.
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """Module 7-base_geometry.
Specifies a BaseGeometry class."""

    def area(self):
        """Throws an Exception with the message area() method is not defined.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
