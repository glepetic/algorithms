def quicksort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    pivot = list_to_sort[0]
    left_values = list()
    right_values = list()

    for elem in list_to_sort[1:len(list_to_sort)]:
        if elem < pivot:
            left_values.append(elem)
        else:
            right_values.append(elem)

    left_sorted_values = quicksort(left_values)
    right_sorted_values = quicksort(right_values)
    left_sorted_values.append(pivot)
    return left_sorted_values + right_sorted_values


test_list = [4, 2, 99, 82, 1, 2, 4, 2, 4, 91, 22, 11, 23, 19, 2, 5, 19, 1]
expected_result = [1, 1, 2, 2, 2, 2, 4, 4, 4, 5, 11, 19, 19, 22, 23, 82, 91, 99]

assert quicksort(test_list) == expected_result
print("True!")
