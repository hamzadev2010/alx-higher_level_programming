#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method for obtaining a dictionary representation.
        If 'attrs' is a list of strings,
        only attribute names contained in this list
        will be retrieved. Otherwise, all attributes will be retrieved."""

        res = {}

        if attrs is None:
            return (self.__dict__)

        for key in attrs:
            """If a key is not found in the class, it returns None. In such a case,
            this class should be transformed into a dictionary."""
            value = self.__dict__.get(key)
            if value is not None:
                res[key] = value

        return (res)
