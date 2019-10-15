#!/usr/bin/python3
"""
Class MyInt

"""


class MyInt(int):
    """ sets an int value to reverse in logic comparison """
    def __eq__(self, value):
        """ negate equal """
        return False

    def __ne__(self, value):
        """ negate nonequal """
        return True
