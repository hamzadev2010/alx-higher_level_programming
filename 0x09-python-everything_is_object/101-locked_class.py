#!/usr/bin/python3
"""present locked Class"""


class LockedClass:
    """
       locked class is the dynamic creation of new instance attributes,
    allowing only the 'first_name'.
    """

    __slots__ = ['first_name']
