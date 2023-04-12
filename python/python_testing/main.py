def add_integer(a, b=98):
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return a + b