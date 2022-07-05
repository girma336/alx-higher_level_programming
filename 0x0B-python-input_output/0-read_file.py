#!/usr/bin/python3
"""Write a function that read a text file encoding='utf-8'"""


def read_file(filename=""):
    """print the content of file name"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
