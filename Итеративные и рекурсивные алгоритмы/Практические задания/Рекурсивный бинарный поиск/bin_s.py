def func_search(arr: list, value: int) -> int:
    ind_a = 0
    ind_b = len(arr) - 1

    while ind_b - ind_a > 0:
        ind_pivot = (ind_b + ind_a) // 2
        current_value = arr[ind_pivot]

        if current_value == value:
            return ind_pivot
        if current_value > value:
            ind_b = ind_pivot - 1
        else:
            ind_a = ind_pivot + 1

    if arr[ind_a] == value:
        return ind_a
    # if arr[ind_b] == value:
    #     return ind_b
    return -1

print(func_search([0,1,2,3,4,5,6,7,8,9,10], 5))

