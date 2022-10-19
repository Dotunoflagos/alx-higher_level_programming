#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Assign the size variable"""
    def __init__(self, size=0):
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
            elif isinstance(size, int) and size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except Exception:
            raise
