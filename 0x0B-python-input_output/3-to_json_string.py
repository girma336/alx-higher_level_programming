#!/usr/bin/python3
"""Write a function that return the JSON representation"""
import json


def to_json_string(my_obj):
    """Json representation of an object (string)"""

    return json.dumps(my_obj)
