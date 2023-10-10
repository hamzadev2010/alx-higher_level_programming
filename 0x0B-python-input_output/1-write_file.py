#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """This function is designed to save a string to a text file
    and then report the count of characters that were written."""

    num_characters = 0

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

    num_characters = len(text)

    return num_characters
