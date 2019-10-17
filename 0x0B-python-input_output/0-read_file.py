#!/usr/bin/python3
"""
Module read_file

"""


def read_file(filename=""):
    """ prints a file line by line """
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
