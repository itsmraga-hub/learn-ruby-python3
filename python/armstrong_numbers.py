def is_armstrong_number(number):
  l = len(str(number))
  sum = 0
  for i in str(number):
    sum += int(i) ** l

  if sum == number:
    return True
  return False


print(is_armstrong_number(10))