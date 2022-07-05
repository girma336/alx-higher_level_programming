#!/usr/bin/python3
"""Write a function that create an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """write the object joson"""

    with open(filename) as f:
        return json.load(f)
