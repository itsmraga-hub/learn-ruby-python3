def leap_year(year):
  """
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
  """
  # mod_four = year % 4
  if year % 4 == 0:
    return True
  elif year % 100 == 0:
    if year % 400 == 0:
      return True
    return False
  else:
    return False

print(leap_year(2100))