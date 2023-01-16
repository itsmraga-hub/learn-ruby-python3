def multiply_by(num):
  def multiply(value):
    print('Value: ', value)
    return num * value

  return multiply

func = multiply_by(5)
print("5 * 10 = ", func(6))

def is_odd(num):
  if num % 2 == 0:
    return False
  return True


def odd_checker(func, list):
  list_of_odds = []
  for i in list:
    if func(i):
      list_of_odds.append(i)

  return list_of_odds


print("Odd numbers: ", odd_checker(is_odd, [9, 2, 4, 5, 7, 8]))