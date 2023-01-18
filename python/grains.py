def create_arr():
  arr = [1, ]
  for i in range(1, 65):
    num = arr[-1] * 2
    # print("{} * 2: {}".format(i, num))
    arr.append(num)
  return arr

def square(number):
  if number >= 1 and number <= 64:
    square_arr = create_arr()
    # print(square_arr[number - 1])
    return square_arr[number - 1]

  else:
    raise ValueError("square must be between 1 and 64")

import functools

def total():
    # sum = 0
    # for i in create_arr():
    #   sum += i

    # return sum
    return functools.reduce(lambda a, b: a + b, create_arr(), 0)

# print(square(3))
print(total())


# print(create_arr())