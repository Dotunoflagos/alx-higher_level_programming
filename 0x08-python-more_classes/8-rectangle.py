#!/usr/bin/python3
"""Creat rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def st(self, value, name=""):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value < 0:
            raise ValueError(f'{name} must be >= 0')
        if name == "width":
            self.__width = value
        elif name == "height":
            self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                strg += str(self.print_symbol)
            if i != self.__height - 1:
                strg += '\n'
        return strg

    def __repr__(self):
        strg = f"Rectangle({self.__width}, {self.__height})"
        return strg

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):

        def ck(rect, x):
            if type(rect) != Rectangle:
                raise TypeError(
                    '{} must be an instance of Rectangle'.format(x)
                    )

        ck(rect_1, "rect_1")
        ck(rect_2, "rect_2")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
