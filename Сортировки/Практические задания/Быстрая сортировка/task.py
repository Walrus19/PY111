from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки
    if len(container) <= 1:
        return container
    pivot = container[len(container) // 2]

    """1-решение"""
    # left = [x for x in container if x < pivot]
    # middle = [x for x in container if x == pivot]
    # right = [x for x in container if x > pivot]

    """2-решение"""
    new_container = container.copy()
    left = []
    for x in container:
        if x < pivot:
            left.append(x)
            new_container.remove(x)

    container = new_container
    middle = []
    for x in container:
        if x == pivot:
            middle.append(x)
            new_container.remove(x)

    right = new_container.copy()

    return sort(left) + middle + sort(right)


def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index + 1, high)


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    container = container.copy()
    quick_sort(container, 0, len(container) - 1)  # TODO реализовать алгоритм быстрой сортировки
    return container

# a = [4,3,5,2,7,5]
# print(sort(a))
# print(a)
#
# sorted([4,3,5,2,7,5])
# [4,3,5,2,7,5].sort()

# print(sort([4,3,5,2,7,5]))
#
# a = [4,3,5,2,7,5]
# print(a)
# quick_sort(a, 0, len(a) - 1)
# print(a)

# print(a)
# index_part = partition(a, 0, len(a)-1)
# print(index_part)
# print(a)
# index_part = partition(a, 0, index_part-1)
# print(index_part)
# print(a)
# index_part = partition(a, index_part+1, 3)
# print(index_part)
# print(a)

