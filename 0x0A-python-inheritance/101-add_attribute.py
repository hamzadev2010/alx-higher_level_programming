#!/usr/bin/python3
"""Specifies a function for adding attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Add a new attribute to an object if feasible.
obj any: The object to which an attribute will be added.
att str : The name of the attribute to be appended to obj.
value any: The value of the attribute.
Raises:
TypeError: If adding the attribute is not possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add the new attribute")
    setattr(obj, att, value)
