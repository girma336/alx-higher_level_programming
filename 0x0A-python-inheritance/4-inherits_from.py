#!/usr/bin/python3
"""Write a Function that return True if ..."""


def inherits_from(obj, a_class):
    """
    args:
        obj@listof an elemrnr
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
