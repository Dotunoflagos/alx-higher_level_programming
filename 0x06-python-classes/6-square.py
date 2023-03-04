#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Assign the size variable"""

    def __init__(self, size=0, position=(0, 0)):
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
                self.__position = position
            elif isinstance(size, int) and size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')

            if not isinstance(position, tuple) \
                    or all(not isinstance(p, int) for p in position):
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            elif len(position) < 0 \
                    or len(position) > 2 or position[0] < 0 or position[1] < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            else:
                self.__position = position
        except Exception as e:
            print(e)

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
        except Exception as e:
            print(e)

    """Returnes area of square"""

    def area(self):
        try:
            if isinstance(self.size, int) and self.size >= 0:
                return self.size ** 2
            elif isinstance(self.size, int) and self.size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except Exception as e:
            print(e)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
