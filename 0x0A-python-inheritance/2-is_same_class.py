#!/usr/bin/python3
""" Write a function that return True"""


def is_same_class(obj, a_class):
    """is same class 0r not"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
