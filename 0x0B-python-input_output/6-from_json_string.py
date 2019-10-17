#!/usr/bin/python3
from json import loads
"""
Module from_json_string

"""


def from_json_string(my_str):
    """ returns an obj represented by JSON str """
    return loads(my_str)
