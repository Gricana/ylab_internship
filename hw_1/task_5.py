from math import prod


def count_find_num(primesL: list, limit: int) -> list:
    """
    Возврашает кол-во найденных чисел в интервале до limit, имеющих простые делители primesL
    :param primesL: list - Простые делители числа
    :param limit: int - Верхняя граница интервала поиска
    :return: list - кол-во найденных чисел и максимальное найденное число
    """
    min_number = prod(primesL)
    result = set()
    result.add(min_number)
    if min_number > limit:
        return []
    old_values = {min_number}

    while min_number <= limit:
        new_values = set()

        for i in old_values:

            for n in primesL:
                mul = i * n
                new_values.add(mul)

                if mul <= limit:
                    result.add(mul)

        min_number = min(new_values)
        old_values = {i for i in new_values if i < limit}

    return [len(result), max(result)]


def test() -> None:
    """
    Запуск тестов для проверки метода count_find_num
    :return: None
    """
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []


if __name__ == '__main__':
    test()
