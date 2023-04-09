def binary_search(ls, value):
    sorted_list = sorted(ls)
    l = len(sorted_list)
    while True:
        mid = len(sorted_list) // 2
        if not sorted_list:
            return "Value not found"
        elif sorted_list[mid] == value:
            return sorted_list[mid]
        elif sorted_list[mid] < value:
            mid += 1
            return binary_search(sorted_list[mid:], value)
        elif sorted_list[mid] > value:
            # mid += 1
            return binary_search(sorted_list[:mid], value)


v = binary_search([1, 23, 15, 60, 8, 9, 11, 4, 2, 0], 23)
print(v)
