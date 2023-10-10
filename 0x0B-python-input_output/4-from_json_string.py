#!/usr/bin/python3
"""4-from_json_string.py"""
import json


def from_json_string(My_str):
    """Function that returns a Python data structure
    object represented by a JSON string."""

    return json.loads(My_str)
