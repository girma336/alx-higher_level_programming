#!/usr/bin/python3
"""square of any size"""


class Square:
    """Square class with TypeError"""

    def __init__(self, size=0):
        """Initialization of square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("sizee must be >= 0")
