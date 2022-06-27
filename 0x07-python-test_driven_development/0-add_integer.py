#!/usr/bin/python3
"""add two numbers"""


def add_integer(a, b=98):
    """the number must be integer or floats"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
