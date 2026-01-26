#!/usr/bin/python3
"""Define a node"""


class Node:
    """Class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        values = []
        ptr = self.__head
        while ptr is not None:
            values.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None:
            self.__head = new
            return

        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        ptr = self.__head
        while ptr.next_node is not None and ptr.next_node.data < value:
            ptr = ptr.next_node

        new.next_node = ptr.next_node
        ptr.next_node = new
