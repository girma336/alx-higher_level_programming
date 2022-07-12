#!/usr/bin/python3
"""Write the class Square that inherites from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    args:
    __id = id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initalize the given or parameter value"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):

        string = "[{}]".format(self.__class__.__name__)
        string += " ({}) {}/{} - {}".format(self.id,
                                            self.x,
                                            self.y, self.size)
        return string

    def update(self, *args, **kwargs):

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return update the dec"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
