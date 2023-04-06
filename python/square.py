class Square:
    def __init__(self, size=0, position=(0, 0)):
        # if type(size) == int and size < 0:
        #     raise ValueError('size must be >= 0')
        # elif type(size) == int:
        #     self.__size = size
        # else:
        #     raise TypeError('size must be an integer')
        self.__size = size
        self.__position = position

    # @size_getter
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    # @size_setter
    @size.setter
    def size(self, size):
        if type(size) == int and size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) == int:
            self.__size = size
        else:
            raise TypeError('size must be an integer')

    @position.setter
    def position(self, position):
        if type(position) == tuple and position[0] > 0 and position[1] > 1:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("\n")