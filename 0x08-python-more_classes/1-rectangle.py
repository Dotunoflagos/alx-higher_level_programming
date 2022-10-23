#!/usr/bin/python3
"""Creat rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __st(self, value, name=""):
        if name == "width":
            str = "width"
        elif name == "height":
            str = "height"

        try:
            if not isinstance(value, int):
                raise TypeError("{} must be an intiger".format(str))
            elif value < 0:
                raise ValueError("{} must be >= 0".format(str))
            else:
                if name == "width":
                    self.__weidth = value
                elif name == "height":
                    self.__height = value
        except Exception:
            raise

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
        return self.__weidth

    @height.setter
    def height(self, value):
        self.__st(value, "height")
