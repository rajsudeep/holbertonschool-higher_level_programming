#!/usr/bin/python3
def islower(c):
    """Checks for a lowercase character."""
    letternum = ord(c)
    if (letternum >= 97 and letternum <= 122):
        return(True)
    return(False)
