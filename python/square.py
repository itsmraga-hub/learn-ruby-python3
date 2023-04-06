class Square:
    def __init__(self, size=0):
        # if type(size) == int and size < 0:
        #     raise ValueError('size must be >= 0')
        # elif type(size) == int:
        #     self.__size = size
        # else:
        #     raise TypeError('size must be an integer')
        self.__size = size

    # @size_getter
    @property
    def size(self):
        return self.__size

    # @size_setter
    @size.setter
    def size(self, size):
        if type(size) == int and size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) == int:
            self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("\n")