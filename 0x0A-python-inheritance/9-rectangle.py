#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
Class Rectangle

"""


class Rectangle(BaseGeometry):
    """ defining rectangle shapes """

    def __init__(self, width, height):
        """ initializes width and height """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """ obtain area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
