#!/usr/bin/python3
from math import factorial


def comb(n, k):
    """ n choose k """
    return int((factorial(n)) / ((factorial(k)) * factorial(n - k)))

def pascal_triangle(n):
    res = []
    for row in range(n):
        seg = []
        for i in range(row + 1):
            seg.append(comb(row, i))
        res.append(seg)

    return res
