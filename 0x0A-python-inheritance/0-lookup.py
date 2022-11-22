#!/usr/bin/python3
"""
Finding a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns that list of attributes and methods.
    """
    return dir(obj)
