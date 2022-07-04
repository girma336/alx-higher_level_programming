#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseG"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherite from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the value of area"""
        return self.__width * self.__height

    def __str__(self):
        """Return print and str representation"""
        cla_name = "[" + str(self.__class__.__name__) + "]"
        cla_name += str(self.__width) + "/" + str(self.__height)
        return cla_name
