from typing import Sequence

# from numpy.ma import count


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """


    min_val = min(container)
    max_val = max(container)
    count_array_size = max_val - min_val + 1
    count_array = [0] * count_array_size

    for number in container:
        count_array[number - min_val] += 1

    sorted_list = []
    for i, count in enumerate(count_array):
        sorted_list.extend([i + min_val] * count)

    return sorted_list

c = [1,2,3,4,2,3,4,5,0]
print(sort(c))
