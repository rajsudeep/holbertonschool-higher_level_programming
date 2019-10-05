#!/usr/bin/python3

"""
This module includes:
text_indentation

"""

def text_indentation(text):
    """
    Prints a reformatted a text with double new line indentation
    """

    txt_err = "text must be a string"

    if not isinstance(text, str):
        raise TypeError(txt_err)

    print_str = ""
    for i in text:
        if i is '.' or i is '?' or i is ':':
            print_str += i
            print(print_str.strip(" "), end="\n\n")
            print_str = ""
        else:
            print_str += i
    print(print_str.strip(" "), end="")
