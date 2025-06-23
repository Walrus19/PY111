from typing import List


def merge(arr_a: list, arr_b: list) -> list:
    res = []
    while True:
        if arr_a[0] <= arr_b[0]:
            res.append(arr_a.pop(0))
        else:
            res.append(arr_b.pop(0))
        if not arr_a:
            res.extend(arr_b)
            return res
        elif not arr_b:
            res.extend(arr_a)
            return res


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализуйте сортировку слиянием
    if len(container) in (0, 1):
        return container

    mid_ind = len(container) // 2
    arr_a = container[:mid_ind]
    arr_b = container[mid_ind:]

    sort_arr_a = sort(arr_a)
    sort_arr_b = sort(arr_b)

    return merge(sort_arr_a, sort_arr_b)



# print(merge([1,2], [4,5]))
# print(merge([1,6], [2, 5, 7, 20]))
# print(merge([6,7], [4,5]))
# print(merge([6], [5]))

# print(sort([4,3,5,2,7]))
