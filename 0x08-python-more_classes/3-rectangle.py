#!/usr/bin/python3

"""
This module contains the Rectangle class
Defines a rectangle

"""


class Rectangle:
    """Rectangle defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Size of width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Size of height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates area of rectangle """
        return (self.width * self.height)

    def perimeter(self):
        """ Calculates perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (2*self.height + 2*self.width)

    def __str__(self):
        """ Print rectangle represented by #s """
        rect_str = ""
        if self.width == 0 or self.height == 0:
            return rect_str
        rect_str = (('#' * self.width) + '\n') * self.height
        return rect_str[:-1]
