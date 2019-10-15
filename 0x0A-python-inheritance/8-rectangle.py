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
