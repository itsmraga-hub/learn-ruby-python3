def classify(number):
  """ A perfect number equals the sum of its positive divisors.

  :param number: int a positive integer
  :return: str the classification of the input integer
  """
  output = []
  for i in range(1, number):
    if number % i == 0:
      output.append(i)
    
  total = 0
  for i in output:
    total += i

  