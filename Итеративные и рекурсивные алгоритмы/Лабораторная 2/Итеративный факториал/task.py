def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
     # TODO реализовать итеративный алгоритм нахождения факториала

    rez = 1
    for i in range(1,n+1):
        rez *= i

    return rez

print(factorial_iterative(5))
