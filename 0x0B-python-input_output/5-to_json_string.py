#!/usr/bin/python3
from json import dumps
"""
Module to_json_string

"""


def to_json_string(my_obj):
    """ serializes obj to json """
    return dumps(my_obj)
