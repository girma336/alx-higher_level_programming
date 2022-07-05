#!/usr/bin/python3
"""Write a function that return the object representation"""
import json


def from_json_string(my_str):
    """Json representation to an object (string) of
    python data structure representation
    """

    return json.loads(my_str)
