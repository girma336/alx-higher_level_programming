#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
            """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

        @property
        def next_node(self):
            """Get/set the next_node of the Node."""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """ singly linked list class"""

    def __init__(self):
        """ initialization"""
        self.__head = None

    def __str__(self):
        """ make list printable"""
        all_data = ""
        tmp = self.__head
        while (tmp):
            all_data += str(tmp.data) + "\n"
            tmp = tmp.next_node
        # return all data except the new line at the end
        return all_data[:-1]

    def sorted_insert(self, value):
        """ insert into correct sorted position"""
        NewNode = Node(value)
        temp = self.__head
        if temp is None:
            self.__head = NewNode
            return
        if value <= temp.data:
            NewNode.next_node = self.__head
            self.__head = NewNode
            return

        while (temp.next_node and temp.next_node.data <= value):
            temp = temp.next_node
        NewNode.next_node = temp.next_node
        temp.next_node = NewNode
