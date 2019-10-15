#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""
Class Square

"""


class Square(Rectangle):
    """ defining rectangle shapes """

    def __init__(self, size):
        """ initializes size of square """
        self.__size = size
        Rectangle.integer_validator(self, "size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ obtain area of square """
        return (self.__size**2)
