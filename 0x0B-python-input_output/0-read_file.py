#!/usr/bin/python3
"""Function to parse a file."""


def read_file(filename=""):
    """This function reads a text file in UTF-8 encoding and
    outputs its content to the standard output (stdout)."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
