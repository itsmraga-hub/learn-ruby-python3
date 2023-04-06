from square import Square

# my_square_1 = Square(3)
# print(type(my_square_1))
# print(my_square_1.__dict__)

# my_square_2 = Square()
# print(type(my_square_2))
# print(my_square_2.__dict__)

# try:
#     print(my_square_1.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square_1.__size)
# except Exception as e:
#     print(e)

# try:
#     my_square_3 = Square("3")
#     print(type(my_square_3))
#     print(my_square_3.__dict__)
# except Exception as e:
#     print(e)

# try:
#     my_square_4 = Square(-89)
#     print(type(my_square_4))
#     print(my_square_4.__dict__)
# except Exception as e:
#     print(e)

# my_square_1 = Square(3)
# print("Area: {}".format(my_square_1.area()))

# try:
#     print(my_square_1.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square_1.__size)
# except Exception as e:
#     print(e)

# my_square_2 = Square(5)
# print("Area: {}".format(my_square_2.area()))


# my_square = Square(89)
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# my_square.size = 3
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# try:
#     my_square.size = "5 feet"
#     print("Area: {} for size: {}".format(my_square.area(), my_square.size))
# except Exception as e:
#     print(e)

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")