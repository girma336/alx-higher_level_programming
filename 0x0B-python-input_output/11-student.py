#!/usr/bin/python3
"""Write a class Student That defines a student by"""


class Student:
    """name of the class was Strudent"""

    def __init__(self, first_name, last_name, age):
        """Initialization of new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """load json to object"""

        for k, v in json.items():
            setattr(self, k, v)
