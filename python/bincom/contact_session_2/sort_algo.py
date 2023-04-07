def sort_algorithm(ls):
    ls_copy = ls


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = [], []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)



sorted_list = quick_sort([1, 7, 9, 5, 4, 3, 2, 1, 4, 5, 8])
print(sorted_list)