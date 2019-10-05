#!/usr/bin/python3

"""
This module contains:
matrix_divided

"""

def matrix_divided(matrix, div):
    """
    Return a new matrix dividing each element by div
    """

    div_err = "div must be a number"
    zero_err = "division by zero"
    row_err = "Each row of the matrix must have the same size"
    mtx_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError(div_err)
    if div == 0:
        raise ZeroDivisionError(zero_err)
    if matrix == [] or matrix == [[]]:
        raise TypeError(mtx_err)

    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(mtx_err)
        if len(row) != row_len:
            raise TypeError(row_err)
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(mtx_err)
    return [[round(i / div, 2) for i in row] for row in matrix]
