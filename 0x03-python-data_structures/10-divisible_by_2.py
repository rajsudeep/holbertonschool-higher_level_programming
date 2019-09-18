#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or my_list == []:
        return None
    bool_list = []
    for i in my_list:
        bool_list.append(True) if (i % 2 == 0) else bool_list.append(False)
    return bool_list
