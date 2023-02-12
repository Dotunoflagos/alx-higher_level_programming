#!/usr/bin/python3
"""
Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.int_validation("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.int_validation("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.int_validation("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.int_validation("y", y)
        self.__y = y

    def int_validation(self, name, value):
        """Validates input"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """Returnes area"""
        return self.height * self.width

    def display(self):
        """Print rectangle"""
        for y in range(self.y):
            print("")
        for x in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for y in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Print rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle"""

        if args:
            length = len(args)
            keys = ["id", "width", "height", "x", "y"]
            newkey = keys[:length]

            for index in range(length):
                value = newkey[index]
                if index > 0:
                    key = "_Rectangle__{}".format(value)
                else:
                    key = "{}".format(value)

                self.__dict__[key] = args[index]
        else:
            for key, value in kwargs.items():
                if key != "id":
                    ke = "_Rectangle__{}".format(key)
                else:
                    ke = "{}".format(key)
                self.__dict__[ke] = value

    def to_dictionary(self):
        """Returs dict rep"""
        dic = self.__dict__
        dic["width"] = dic.pop("_Rectangle__width")
        dic["height"] = dic.pop("_Rectangle__height")
        dic["x"] = dic.pop("_Rectangle__x")
        dic["y"] = dic.pop("_Rectangle__y")
        return dic
