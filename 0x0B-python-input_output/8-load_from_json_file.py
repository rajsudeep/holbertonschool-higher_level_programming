#!/usr/bin/python3
from json import load
"""
Module load_from_json_file

"""


def load_from_json_file(filename):
    """ creates an obj from a json file """
    with open(filename, 'r', encoding="UTF-8") as f:
        return load(f)
