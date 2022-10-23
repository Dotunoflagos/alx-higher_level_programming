#!/usr/bin/python3
"""Creat rectangle class"""


class Rectangle:
    """Rectangle class"""
    def st(self, value, name=""):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an intiger')
        elif value < 0:
            raise ValueError(f'{name} must be >= 0')

        if name == "width":
            self.__weidth = value
        elif name == "height":
            self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an intiger')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an intiger')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
