#!/usr/bin/python3

"""
This module includes:
say_my_name

"""

def say_my_name(first_name, last_name=""):
    """
    Print a first and last name
    """

    first_err = "first_name must be a string"
    last_err = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(first_err)
    if not isinstance(last_name, str):
        raise TypeError(last_err)
    say_name = "My name is " + first_name + " " + last_name
    print(say_name)
