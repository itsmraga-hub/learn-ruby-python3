def leap_year(year):
  """
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
  """
  mod_four = year // 4
  mod_hund = year // 100
  mod_four_hund = year // 400
  print(mod_four)
  print(mod_hund)
  print(mod_four_hund)

  if mod_four % 2 == 0 and mod_hund % 2 == 0:
     

  # if mod_four % 2 == 0:
  #   if mod_hund % 2 == 0:
  #     if mod_four_hund % 2 == 0:
  #       return True
  #     return False
  #   return True
  # else:
  #   return False

# print(leap_year(2100))
print(leap_year(1996))
print(leap_year(2000))