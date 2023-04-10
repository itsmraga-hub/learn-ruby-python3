"""
    A module defining a Rectnagle class
"""


class Rectangle:
    """A class defining a Rectangle"""
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        for j in range(self.height):
            for i in range(self.width):
                print('#', end="")
            print()
        return ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
