#!/usr/bin/python3
def handle_sm_tuple(tuple_list):
    if len(tuple_list) < 2:
        if len(tuple_list) == 1:
            tuple_list.append(0)
        else:
            tuple_list.extend([0, 0])


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    handle_sm_tuple(list_a)
    handle_sm_tuple(list_b)
    a_sum = list_a[0] + list_b[0]
    b_sum = list_a[1] + list_b[1]
    return (a_sum, b_sum)
