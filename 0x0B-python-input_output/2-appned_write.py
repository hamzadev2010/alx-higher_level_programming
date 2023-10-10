#!/usr/bin/python3
"""Function that generates a JSON
representation of an object and returns it as a string.
"""

def append_write(filename="", text=""):
    """
write_file - Adds a string to the end of a text file
in UTF-8 encoding and returns the count of characters written:
filename: The file name.
text: The text to append.
Returns: The number of characters written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))

