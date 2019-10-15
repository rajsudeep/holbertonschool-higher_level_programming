#!/usr/bin/python3
"""
Class BaseGeometry

"""


class BaseGeometry:
    """ defining geometry shapes """

    def area(self):
        """ currently not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
