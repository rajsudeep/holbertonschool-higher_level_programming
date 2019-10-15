#!/usr/bin/python3
"""
Module inherits_from

"""


def inherits_from(obj, a_class):
    """return true iff obj is an instance of a_class"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
