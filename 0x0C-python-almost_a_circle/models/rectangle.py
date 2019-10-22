#!/usr/bin/python3
"""
Class Rectangle -
defines a rectangle

"""

from models.base import Base


class Rectangle(Base):
    """ defines a rectangle """
    print_symbol = '#'
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of a rectangle """
        return self.__height * self.__width

    def display(self):
        """ project the rectangle using hashes """
        row = (' ' * self.__x) + (Rectangle.print_symbol * self.__width) + '\n'
        print(('\n' * self.__y) + (row * self.__height), end="")

    def __str__(self):
        """ string representation of rectangle """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ helper to update attributes """
        arg = [id, width, height, x, y]
        var = ["id", "width", "height", "x", "y"]
        for i in range(5):
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
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y":self.__y}
