#!/usr/bin/python3
"""11-student.py"""


class Student:
    """class of student"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method for obtaining a dictionary representation. If 'attrs' is a list of strings,
        only attribute names contained in this list are retrieved;
        otherwise, all attributes are included"""

        res = {}

        if attrs is None:
            return (self.__dict__)

        for key in attrs:
            """If not find key in the class return None, for that
            this class should be transform in dictionary"""
            value = self.__dict__.get(key)
            if value is not None:
                res[key] = value
        return (res)

    def reload_from_json(self, json):
        """A method that replaces all attributes of the student instance."""

        dict_new = self.__dict__

        for key, value in json.items():
            if (dict_new.get(key) == self.first_name):
                self.first_name = value
            elif (dict_new.get(key) == self.last_name):
                self.last_name = value
            elif (dict_new.get(key) == self.age):
                self.age = value
