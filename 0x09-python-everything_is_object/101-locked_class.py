#!/usr/bin/python3
"""
Class that demonstrates restricting
user from creating new instance attrs

"""


class LockedClass:
    """
    Restrict how user creats new instances
    """
    __slots__ = 'first_name'

    def __init__(self):
        pass
