#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """A function that constructs an object from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
