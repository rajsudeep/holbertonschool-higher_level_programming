#!/usr/bin/python3
"""
Module read_lines

"""


def read_lines(filename="", nb_lines=0):
    """ prints n lines of a file """
    with open(filename, 'r', encoding="UTF-8") as f:
        lines = 0
        if nb_lines <= 0:
            print(f.read(), end='')
            for n in f:
                if lines < nb_lines:
                    print(n, end='')
                    lines += 1
