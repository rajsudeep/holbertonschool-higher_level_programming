#!/usr/bin/python3
"""
Module class_to_json

"""


def class_to_json(obj):
    """ returns dictionary description of json obj """
    return obj.__dict__
