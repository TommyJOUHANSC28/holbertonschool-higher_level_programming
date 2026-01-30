#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """Class Rectangle that defines a square."""

    def __init__(self, width=0, height=0):
        """Mehod to initialize the square object

           Args:
            width: rectangle width
            height: rectangle height

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

    def area(self):
        """Method  that returns the rectangle area
        """
        return ((self.__height) * (self.__width))

    def perimeter(self):
        """that returns the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Methode that  return 2 * (self.__height + self.__width)
        Returns:
               str of the rectangle
        """
        if self.width == 0 or self.height == 0:
            print("")
            return 0
        lines = []
        for i in range(self.height):
            lines.append("#" * self.width)
        return ("\n".join(lines))

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """

        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Methode that print the message Bye rectangle...
           when an instance of Rectangle is deleted
           """
        print("Bye rectangle...")
