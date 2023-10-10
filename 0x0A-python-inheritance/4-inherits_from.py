#!/usr/bin/python3
"""Defines a function for checking inherited classes."""


def inherits_from(obj, a_class):
    """"Validates whether an object is an inherited instance of a class.
Args: obj (any): The object under examination.
a_class (type): The class for which the type of obj is assessed.
Returns:True if obj is an inherited instance of
a_class; otherwise, False."
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
