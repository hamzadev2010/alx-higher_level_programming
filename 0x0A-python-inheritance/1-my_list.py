#!/usr/bin/python3
"""
the MyList class
"""


class MyList(list):
    """ subclass list"""
    def __init__(self):
        """initializ object"""
        super().__init__()

    def print_sorted(self):
        """display the sorted list"""
        print(sorted(self))
