"""
    A module defining a Rectnagle class
"""


class Rectangle:
    """A class defining a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1


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
                print(self.print_symbol, end="")
            print()
        return ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye Rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            
    @classmethod
    def square(cls, size=0):
        """Return new Rectangle with width==height==size"""
        if not isinstance(size, int):
            raise TypeError("size has to be an integer")
        elif size < 0:
            raise TypeError("size has to be >= 0")
        else:
            square = Rectangle(size, size)
            return square

