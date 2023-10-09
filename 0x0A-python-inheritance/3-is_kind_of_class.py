#!/usr/bin/python3
# Auth: Sangwani P Zyambo

"""  definition a function that returns True if object intance otherwise false

"""


def is_kind_of_class(obj, a_class):
    """ Returns true if the object is an instace of a class"""

    if isinstance(obj, a_class):
        return True
    return False
