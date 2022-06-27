#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """Define the impelimentation of rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property retrive the width"""
        return self.__width

    @property
    def height(self):
        """property reterive the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """retrive the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Retrive the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return the hashtag in rectangle form"""
        if self.__width == 0 or self.__height == 0:
            return ""

        my_re = []

        for i in range(self.__height):
            [my_re.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                my_re.append("\n")
        return ("".join(my_re))
