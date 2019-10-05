#!/usr/bin/python3

"""
This module includes:
def_square

"""

def print_square(size):
    """
    Prints a square represented by hashtags
    """
    int_err = "size must be an integer"
    val_err = "size must be >= 0"
    float_err = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(int_err)
    if size < 0:
        raise TypeError(val_err)
    if isinstance(size, float) and size < 0:
        raise TypeError(float_err)

    for i in range(size):
        print('#' * size)
