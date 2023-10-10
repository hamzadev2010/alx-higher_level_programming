#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_object, filename):
    """A function that saves an object to a text file using its JSON representation."""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_object))
