#!/usr/bin/python3
"""
Class Square -
defines a square

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a square """
    print_symbol = '#'

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ set size of square """
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of rectangle """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def __update(self, id=None, size=None, x=None, y=None):
        """ helper to update attributes """
        arg = [id, size, x, y]
        var = ["id", "size", "x", "y"]
        for i in range(4):
            if arg[i] is not None:
                setattr(self, var[i], arg[i])

    def update(self, *args, **kwargs):
        """ update a rectangle's attributes """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a rectangle """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
