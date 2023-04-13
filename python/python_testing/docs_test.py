# Python Testing

# TODO: Task 0

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


# TODO: Task 1

def matrix_divided(matrix, div):
    for ls in matrix:
        for item in ls:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix mst be a matrix (list of lists) of integers/floats")

    if any(len(ls) != len(matrix[0]) for ls in matrix):
        raise TypeError("Each row of the matrixmust have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
      
    if div == 0:
        raise ZeroDivisionError("division by zereo")

    new_matrix = []
    for ls in matrix:
        inner_ls = []
        for item in ls:
            item = item / div
            inner_ls.append(round(item, 2))
        new_matrix.append(inner_ls)
    
    return new_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# print(matrix_divided(matrix, 3))
# print(matrix)