#!/usr/bin/python3
"""inherits_from module.
Contains a function that performs
a comparison between an object and an instance.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a
class that derived directly otherwise not directly 
from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
