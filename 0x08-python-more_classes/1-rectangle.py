#!/usr/bin/python3
"""Creat rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __st(self, value, name=""):
        if name == "width":
            str = "width"
        elif name == "height":
            str = "height"

        if not isinstance(value, int):
            raise TypeError(f"{str} must be an intiger")
        elif value < 0:
            raise ValueError(f"{str} must be >= 0")
        else:
            if name == "width":
                self.__weidth = value
            elif name == "height":
                self.__height = value

    def __init__(self, width=0, height=0):
        self.__st(width, "width")
        self.__st(height, "height")

    @property
    def width(self):
        return self.__weidth

    @width.setter
    def width(self, value):
        self.__st(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__st(value, "height")
