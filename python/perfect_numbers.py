def classify(number):
  """ A perfect number equals the sum of its positive divisors.

  :param number: int a positive integer
  :return: str the classification of the input integer
  """
  if number <= 0:
    raise ValueError("Classification is only possible for positive integers.")
  else:
    output = []
    for i in range(1, number):
      if number % i == 0:
        output.append(i)
      
    total = 0
    for i in output:
      total += i

    if total == number:
      return "perfect"
    elif total < number:
      return "deficient"
    elif total > number:
      return "abundant"


print(classify(0))