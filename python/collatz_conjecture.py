def steps(number):
  if not isinstance(number, int):
    raise ValueError("Only positive integers are allowed")
  
  count = 0
  while number != 1:
    if number % 2 == 0:
      number = number // 2
    else:
      number = (3 * number) + 1

    count += 1

  return count


print(steps(12))
print(steps(1000000))