#!/usr/bin/python3
"""Write a class Student That defines a student by"""


class Student:
    """name of the class was Strudent"""

    def __init__(self, first_name, last_name, age):
        """Initialization of new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
