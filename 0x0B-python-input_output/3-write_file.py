#!/usr/bin/python3
"""
Module write_file

"""


def write_file(filename="", text=""):
    """ write to a file """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
