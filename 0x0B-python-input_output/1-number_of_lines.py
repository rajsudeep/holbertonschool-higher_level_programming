#!/usr/bin/python3
"""
Module number_of_lines

"""


def number_of_lines(filename=""):
    """ returns the number of lines in a file """
    with open(filename, 'r', encoding="UTF-8") as f:
        return sum(1 for line in f)
