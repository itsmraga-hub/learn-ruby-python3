def square_of_sum(number):
  sum_square = 0
  for i in range(1, number + 1):
    sum_square += i

  return sum_square ** 2



def sum_of_squares(number):
  sum_squares = 0
  for i in range(1, number + 1):
    sq = i ** 2
    sum_squares += sq

  return sum_squares

def difference_of_squares(number):
  return square_of_sum(number) - sum_of_squares(number)


print(difference_of_squares(10))
print(square_of_sum(10))
print(sum_of_squares(10))