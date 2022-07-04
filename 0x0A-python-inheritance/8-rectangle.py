#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseG"""


class BaseGeometry:
    """Write a class Rectangle"""

    def area(self):
        """area of element"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} nust be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """inherite from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
