from rectangle import Rectangle

# Task 0

# my_rectangle = Rectangle()
# print(type(my_rectangle))
# print(my_rectangle.__dict__)

# Task 1

# my_rectangle = Rectangle(2, 4)
# print(my_rectangle.__dict__)

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle.__dict__)

# Task 2

# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Task 3

# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# print(str(my_rectangle))
# print(repr(my_rectangle))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle)
# print(repr(my_rectangle))


# Task 4

# my_rectangle = Rectangle(2, 4)
# print(str(my_rectangle))
# print("--")
# print(my_rectangle)
# print("--")
# print(repr(my_rectangle))
# print("--")
# print(hex(id(my_rectangle)))
# print("--")

# create new instance based on representation
# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# print(new_rectangle)
# print("--")
# print(repr(new_rectangle))
# print("--")
# print(hex(id(new_rectangle)))
# print("--")

# print(new_rectangle is my_rectangle)
# print(type(new_rectangle) is type(my_rectangle))


# Task 5

# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# del my_rectangle

# try:
#     print(my_rectangle)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))


# Task 6

# my_rectangle_1 = Rectangle(2, 4)
# my_rectangle_2 = Rectangle(2, 4)
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# del my_rectangle_1
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# del my_rectangle_2
# print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))


# Task 7

# my_rectangle_1 = Rectangle(8, 4)
# print(my_rectangle_1)
# print("--")
# my_rectangle_1.print_symbol = "&"
# print(my_rectangle_1)
# print("--")

# my_rectangle_2 = Rectangle(2, 1)
# print(my_rectangle_2)
# print("--")
# Rectangle.print_symbol = "C"
# print(my_rectangle_2)
# print("--")

# my_rectangle_3 = Rectangle(7, 3)
# print(my_rectangle_3)

# print("--")

# my_rectangle_3.print_symbol = ["C", "is", "fun!"]
# print(my_rectangle_3)

# print("--")


# Task 8

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")