#!/usr/bin/python3
def sym(sym):
    if (sym == 'I'):
        return 1
    if (sym == 'V'):
        return 5
    if (sym == 'X'):
        return 10
    if (sym == 'L'):
        return 50
    if (sym == 'C'):
        return 100
    if (sym == 'D'):
        return 500
    if (sym == 'M'):
        return 1000
    return 0


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    summ, i = 0, 0
    while (i < len(roman_string)):
        if (i + 1 < len(roman_string)):
            if (sym(roman_string[i]) >= sym(roman_string[i + 1])):
                summ += sym(roman_string[i])
                i += 1
            else:
                summ += sym(roman_string[i + 1]) - sym(roman_string[i])
                i += 2
        else:
            summ += sym(roman_string[i])
            i += 1
    return summ
