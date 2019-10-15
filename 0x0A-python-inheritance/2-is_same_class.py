#!/usr/bin/python3
"""
Module is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns bool of if instance is of said class
    """
    return (type(obj) is a_class)
