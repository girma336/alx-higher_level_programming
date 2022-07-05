#!/usr/bin/python3
"""Write a function that writes an object to a text"""
import json


def save_to_json_file(my_obj, filename):
    """Object to a text file using a Json rep"""

    with open(filename, "w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
