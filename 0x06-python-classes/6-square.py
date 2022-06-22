#!/usr/bin/python3
""" Define Square Class """


class Square:

    """ Blue print for square objects"""
    def __init__(self, size=0, position=(0, 0)):

        """ initialize new objects
        Args:
            size(int): size of new object
        """
        self.size = size
        self.position = position

    @property
    def size(self):

        """ Get size of object"""
        return self.__size

    @size.setter
    def size(self, value):

        """ set size of new object
        Args:
            value(int): size of new object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        """ Get position """
        return self.__position

    @position.setter
    def position(self, value):

        """ set position of square object
        Args:
            value(tuple): new position tuple
        """
        if not isinstance(value, tuple) or len(value) != 2\
                or any(not isinstance(i, int) for i in value)\
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """ Calculate area of square object"""
        return self.__size * self.__size

    def my_print(self):

        """ print square with # symbol"""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for k in range(self.__position[0])]
                [print("#", end="") for j in range(self.__size)]
                print()
