#!/usr/bin/python3
def uppercase(str):
    """Converts lowercase chars in a string to uppercase and prints."""
    for c in str:
        letternum = ord(c)
        if (letternum >= 97 and letternum <= 122):
            c = chr(letternum - 32)
        print("{}".format(c), end='')
    print("")
