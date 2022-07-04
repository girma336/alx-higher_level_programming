#!/usr/bin/python3
"""Write a class Myint"""


class MyInt(int):
    """that inherits from int"""

    def __eq__(self, value):
        """Return True or false"""
        return self.real != value

    def __ne__(self, value):
        """return True of False"""
        return self.real == value
