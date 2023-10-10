#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    '''A method for adding text after finding a specified search string.'''
    line = []
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readlines()
        i = 0
        while i < len(line):
            if search_string in line[i]:
                line[i:i + 1] = [line[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line)
