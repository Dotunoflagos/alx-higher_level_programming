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
