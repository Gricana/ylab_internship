from math import log


def zeros(n: int) -> int:
    """
    Нахождение кол-ва нулей в хвосте значения факториала неотрицательного числа
    :param n: int - число для факториала
    :return: int - число нулей в хвосте факториала
    """
    if n == 0:
        return 0
    k_max = int(log(n, 5))
    count_zeros = int(sum((n / 5 ** i for i in range(1, k_max + 1))))
    return count_zeros


def test():
    """
    Тесты на проверку правильности выполнения функции zeros
    :return: None
    """
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


if __name__ == '__main__':
    test()
