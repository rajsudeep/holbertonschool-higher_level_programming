#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = None
    first_char = None if length == 0 else sentence[0]
    return (length, first_char)
