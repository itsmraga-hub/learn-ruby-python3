def add_integer(a, b=98):
    """
      >>> add_integer(8)
      106
      >>> add_integer(3, 6.0)       
      9
      >>> add_integer(3, '6.0') 
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 6, in add_integer
      TypeError: b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


add_integer(4, 6)