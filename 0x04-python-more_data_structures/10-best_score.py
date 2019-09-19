#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is {}:
        return None
    max = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary.get(max):
            max = key
    return max
