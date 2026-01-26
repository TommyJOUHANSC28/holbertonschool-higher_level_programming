#!/usr/bin/python3
"""Define a square"""


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that return the curent area
        """
        return (self.__size ** 2)

    def size(self):
        """ Getter method to return the size value
        """
        return (self.__size)

    def size(self, value):
        """Setter method to set the size value of the square object
        """
        if not isinstance(val4, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
