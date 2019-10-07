#!/usr/bin/python3

"""
This module contains the Rectangle class
Defines a rectangle

"""


class Rectangle:
    """Rectangle defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances +=1

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

    def bigger_or_equal(rect_1, rect_2):
        """ Compares area of two rectangles and returns the bigger one """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """ Print rectangle represented by #s """
        rect_str = ""
        if self.width == 0 or self.height == 0:
            return rect_str
        rect_str = ((Rectangle.print_symbol * self.width) + '\n') * self.height
        return rect_str[:-1]

    def __repr__(self):
        """ Print absolute rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Delete rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
