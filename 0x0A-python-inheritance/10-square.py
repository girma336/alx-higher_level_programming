#!/usr/biin/python3
"""Write a class Square that inherits from Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """instantiation with size of par"""

    def __init__(self, size):
        """must be private no geter and seter"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
