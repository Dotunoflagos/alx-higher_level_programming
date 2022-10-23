#!/usr/bin/python3
"""Creat rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    
    def st(self, value, name=""):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value < 0:
            raise ValueError(f'{name} must be >= 0')
        if name == "width":
            self.__width = value
        elif name == "height":
            self.__height = value
        number_of_instances += 1

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.st(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.st(value, "height")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height) * 2 + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        strg = ""
        for i in range(self.__height):
            for j in range(self.__width):
                strg += '#'
            if i != self.__height - 1:
                strg += '\n'
        return strg

    def __repr__(self):
        strg = f"Rectangle({self.__width}, {self.__height})"
        return strg

    def __del__(self):
        print('Bye rectangle...')
        number_of_instances -= 1
