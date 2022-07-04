#!/usr/bin/python3
"""Class and inheritancpass"""


class MyList(list):
    """ Inherted class"""

    def print_sorted(self):
        """function publice"""
        print(sorted(self))
