from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    mem_path = {(0, 0): [(0, 0)]}
    coast = table.copy()
    n, m = len(coast), len(coast[0])

    for row_index in range(n-1):
        coast[row_index + 1][0] += coast[row_index][0]
        mem_path[(row_index + 1, 0)] = mem_path[(row_index, 0)] + [(row_index + 1, 0)]

    for col_index in range(m-1):
        coast[0][col_index + 1] += coast[0][col_index]
        mem_path[(0, col_index + 1)] = mem_path[(0, col_index)] + [(0, col_index + 1)]

    for i in range(1, n):
        for j in range(1, m):
            min_value, min_cell = min((coast[i-1][j], (i-1, j)), (coast[i][j-1], (i, j-1)),)# (coast[i-1][j-1], (i-1, j-1)))
            coast[i][j] += min_value
            mem_path[(i, j)] = mem_path[min_cell] + [(i, j)]

    # return coast, mem_path
    return coast


    ...  # TODO рассчитать таблицу стоимостей перемещений


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    # total_coasts, paths = rocket_coasts(coasts_ceil)
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts)
    # print(paths[(2, 3)])
    print(total_coasts[-1][-1])  # 21

