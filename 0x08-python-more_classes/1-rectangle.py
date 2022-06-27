#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle

"""


class Rectangle:
    """class name define by Rectangle"""

    def __init__(self, width=0, height=0):
        """intalization of width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retirive the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Property setter, for setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integre")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """property setter, for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
