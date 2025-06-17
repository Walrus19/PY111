def func_search(arr: list, value: int, ind_a, ind_b) -> int:
    if ind_a > ind_b:
        return -1

    ind_pivot = (ind_b + ind_a) // 2
    current_value = arr[ind_pivot]

    if current_value == value:
        while True:
            if ind_pivot - 1 >= 0 and arr[ind_pivot - 1] == value:
                ind_pivot -= 1
            else:
                return ind_pivot
    if current_value > value:
        ind_b = ind_pivot - 1
    else:
        ind_a = ind_pivot + 1
    # print(ind_a, ind_b)
    return func_search(arr, value, ind_a, ind_b)

print(func_search([1,3,3,3,3,3,3,3,3,4,5,6,7,8,9,10], 0, 0, 15))

