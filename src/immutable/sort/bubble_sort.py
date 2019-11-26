def bubble_sort(list_to_sort):
    cloned_list = list_to_sort.copy()
    swapped = False

    for i in range(0, len(cloned_list)):
        if i+1 < len(cloned_list):
            left = cloned_list[i]
            right = cloned_list[i + 1]
            if right < left:
                swapped = True
                cloned_list[i] = right
                cloned_list[i + 1] = left

    return bubble_sort(cloned_list) if swapped else cloned_list


test_list = [4, 2, 99, 82, 1, 2, 4, 2, 4, 91, 22, 11, 23, 19, 2, 5, 19, 1]
expected_result = [1, 1, 2, 2, 2, 2, 4, 4, 4, 5, 11, 19, 19, 22, 23, 82, 91, 99]


assert bubble_sort(test_list) == expected_result
print("True!")
