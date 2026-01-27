#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """Class Rectangle that defines a square."""

    def __init__(self, width=0, height=0):
        """Mehod to initialize the square object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to return the value of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Method that sets the position value of a rectangle objet
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method to return the value of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Method that sets the position value of a rectangle objet
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
