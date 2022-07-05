#!/usr/bin/python3
"""Write a function that write a string to a text file"""


def write_file(filename="", text=""):
    """return number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
