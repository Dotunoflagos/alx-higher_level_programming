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

    """Returnes size of square"""
    @property
    def size(self):
        return self.__size

    """Changes values """
    @size.setter
    def size(self, value):
        try:
            if isinstance(value, int) and value >= 0:
                self.__size = value
            elif isinstance(value, int) and value < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except Exception:
            raise

    """Returnes area of square"""
    def area(self):
        try:
            if isinstance(self.size, int) and self.size >= 0:
                return self.size ** 2
            elif isinstance(self.size, int) and self.size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except Exception:
            raise
