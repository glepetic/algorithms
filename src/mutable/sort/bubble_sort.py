def bubble_sort(list_to_sort):
    swapped = False

    for i in range(0, len(list_to_sort)):
        if i+1 < len(list_to_sort):
            left = list_to_sort[i]
            right = list_to_sort[i + 1]
            if right < left:
                swapped = True
                list_to_sort[i] = right
                list_to_sort[i + 1] = left

    if swapped:
        bubble_sort(list_to_sort)


test_list = [4, 2, 99, 82, 1, 2, 4, 2, 4, 91, 22, 11, 23, 19, 2, 5, 19, 1]
expected_result = [1, 1, 2, 2, 2, 2, 4, 4, 4, 5, 11, 19, 19, 22, 23, 82, 91, 99]

bubble_sort(test_list)
assert test_list == expected_result
print("True!")
