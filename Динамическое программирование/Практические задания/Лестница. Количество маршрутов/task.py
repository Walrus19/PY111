from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени
    if count_stairs < 0:
        raise ValueError()

    if count_stairs == 0:
        return [0]

    if count_stairs == 1:
        return [0 , 1]

    matrix_state = [0 ,1 ]+[0]*(count_stairs - 1)
    for i in range(2, count_stairs+1):
        matrix_state[i] = matrix_state[i - 1] + matrix_state[i-2]

    return matrix_state

if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
