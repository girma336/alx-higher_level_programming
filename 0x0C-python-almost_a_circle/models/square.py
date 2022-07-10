#!/usr/bin/pythn3
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
            for val in range(len(args)):
                if val == 0:
                    if args[val] is None:
                        self.__init__(self.size, self.x,
                                      self.y)
                    else:
                        self.id = args[val]
                elif val == 1:
                    self.size = args[val]
                elif val == 2:
                    self.x = args[val]
                elif val == 3:
                    self.y = args[val]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return update the dec"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
