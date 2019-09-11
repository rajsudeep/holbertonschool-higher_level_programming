#!/usr/bin/python3
def uppercase(str):
    """Converts lower chars in a str to upper and prints."""
    for c in str:
        letternum = ord(c)
        if (letternum >= 97 and letternum <= 122):
            c = chr(letternum - 32)
        print("{}".format(c), end='')
    print("")
