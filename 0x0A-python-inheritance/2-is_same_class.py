#!/usr/bin/python3
"""
Check if an object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Function to determine if obj is an instance of a_class.
    """

    if(isinstance(obj, a_class)):
        return True
    else:
        return False
