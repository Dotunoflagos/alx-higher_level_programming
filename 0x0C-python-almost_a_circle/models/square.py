#!/usr/bin/python3
"""
Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, size):
        self.int_validation("width", size)
        self._Rectangle__width = size
        self._Rectangle__height = size

    def __str__(self):
        """Print Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update rectangle"""

        if args:
            length = len(args)
            keys = ["id", "size", "x", "y"]
            newkey = keys[:length]

            for index in range(length):
                value = newkey[index]
                if index == 1:
                    self.size = args[index]
                    continue
                elif index > 0:
                    key = "_Rectangle__{}".format(value)
                else:
                    key = "{}".format(value)

                self.__dict__[key] = args[index]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                    continue
                elif key != "id":
                    ke = "_Rectangle__{}".format(key)
                else:
                    ke = "{}".format(key)

                self.__dict__[ke] = value

    def to_dictionary(self):
        dic = self.__dict__
        dic.pop("_Rectangle__width")
        dic["size"] = dic.pop("_Rectangle__height")
        dic["x"] = dic.pop("_Rectangle__x")
        dic["y"] = dic.pop("_Rectangle__y")
        return dic
