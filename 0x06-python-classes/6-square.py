#!/usr/bin/python3


class Square:
    """ Square with a size property area function

    Attributes:
    size (int): Size of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position of square. """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
            type(value[0]) is not int or type(value[1]) is not int or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area of the square

        Returns:
        Area of square

        """
        return self.__size**2

    def my_print(self):
        """ Prints the square size in the form
        of hashtags and spaced relative to position
        value

        """

        if self.__size is 0:
            print("")
        else:
            if self.__position[1] > 0:
                for j in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
