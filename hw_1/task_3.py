def zeros(n: int) -> int:
    """
    Нахождение кол-ва нулей в хвосте значения факториала неотрицательного числа
    :param n: int - число для факториала
    :return: int - число нулей в хвосте факториала
    """
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


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
