#!/usr/bin/python3
"""
Module append_write

"""


def append_write(filename="", text=""):
    """ write to end of file """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
