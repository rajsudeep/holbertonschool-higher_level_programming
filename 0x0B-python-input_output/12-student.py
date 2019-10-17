#!/usr/bin/python3
"""
Class Student

"""


class Student:
    """
    Attributes:
    first_name - first name
    last_name - last name
    age - age

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if all(isinstance(elem, basestring) for elem in attrs):
            return attrs.__dict__
        return self.__dict__
