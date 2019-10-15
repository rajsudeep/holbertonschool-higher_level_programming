#!/usr/bin/python3
"""
module: add_attribute

"""

def add_attribute(obj, key, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, key, value)
    else:
        raise TypeError("can\'t add new attribute")
