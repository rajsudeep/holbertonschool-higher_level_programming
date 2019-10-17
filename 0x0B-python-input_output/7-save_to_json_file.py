#!/usr/bin/python3
from json import dumps
"""
Module save_to_json_file

"""


def save_to_json_file(my_obj, filename):
    """ writes obj to file using JSON """
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(dumps(my_obj))
