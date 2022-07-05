#!/usr/bin/python3
"""Write a function that append a string at the end of a text"""


def append_write(filename="", text=""):
    """return number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
