#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    for i in str_list:
        if (i == 'c') or (i == 'C'):
            str_list.remove(i)
    return ''.join(str_list)
