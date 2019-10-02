#!/usr/bin/python3


class Square:
    """ Square with a size property area function

    Attributes:
    size (int): Size of the square

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of the square

        Returns:
        Area of square

        """
        return self.__size**2
