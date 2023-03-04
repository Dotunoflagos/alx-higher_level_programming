#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Assign the size and position variables"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Returns size of square"""
    @property
    def size(self):
        return self.__size

    """Sets the size of square"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    """Returns position of square"""
    @property
    def position(self):
        return self.__position

    """Sets the position of square"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int) or value[0] < 0 \
                or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    """Returns area of square"""

    def area(self):
        return self.__size ** 2

    """Prints square using # character"""

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        return self.my_print()
