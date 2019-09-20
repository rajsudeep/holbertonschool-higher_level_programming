#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    summ, freq = 0, 0
    for (x, y) in my_list:
        summ += x * y
        freq += y
    return (summ / freq)
