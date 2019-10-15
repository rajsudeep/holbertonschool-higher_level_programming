#!/usr/bin/python3
"""
Module is_kind_of_class

"""


def is_kind_of_class(obj, a_class):
    """ returns bool on if obj is instance/inherited
    from said class
    """
    return isinstance(obj, a_class)
