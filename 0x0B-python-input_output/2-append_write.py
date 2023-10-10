#!/usr/bin/python3
"""2-append_write.py
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
