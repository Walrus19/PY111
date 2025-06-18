"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
     # TODO реализовать итеративный линейный поиск

    if not arr:
        raise ValueError()

    min = arr[0]
    index = 0
    for idx, value in enumerate(arr):
        if value < min:
            min = value
            index = idx

    return index
# arr= [4,2,3,1,5,5,8]
# print(min_search(arr))
