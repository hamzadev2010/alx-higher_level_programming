#!/usr/bin/python3

"""check if object if instance of a class that"""

def inherits_from(obj, a_class):
    """true object is an instance of the class that
    inherited """

    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
