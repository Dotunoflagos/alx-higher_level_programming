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

    def my_print(self):
        len = self.__size
        pos = self.__position
        if len == 0:
            print("")
        i = 0
        while i < len:
            j = 0
            k = 0
            if not pos[1] > 0:
                while k < pos[0]:
                    print(' ', end='')
                    k += 1

            while j < len:
                print('#', end='')
                j += 1

            print('\n', end='')
            i += 1
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        try:
            if not type(value) == tuple:
                raise TypeError('position must be a tuple of 2 positive integers')
            elif len(value) < 2 or len(value) > 2 or value[0] < 0 or value[1] < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
            else:
                self.__position = value
        except TypeError:
            raise

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")