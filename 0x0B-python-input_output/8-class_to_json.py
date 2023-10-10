#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """A function that provides a dictionary description with simple data structures
    list, dictionary, string, integer, and boolean
    for the purpose of JSON serialization of an object."""

    return obj.__dict__
