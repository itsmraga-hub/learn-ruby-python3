def convert(number):
  output = ''
  if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    output = 'PlingPlangPlong'
  elif number % 3 == 0 and number % 5 == 0:
    output = 'PlingPlang'
  elif number % 5 == 0 and number % 7 == 0:
    output = 'PlangPlong'
  elif number % 7 == 0 and number % 3 == 0:
    output = 'PlingPlong'
  elif number % 3 == 0:
    output = 'Pling'
  elif number % 5 == 0:
    output = 'Plang'
  elif number % 7 == 0:
    output = 'Plong'
  else:
    output = "{}".format(number)

  return output


print(convert(15))