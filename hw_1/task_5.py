def get_prime_divisors(n: int) -> set:
    """
    Возврашает уникальные простые делители числа
    :param n: int - Число для поиска его делителе
    :return: set - Делители числа
    """
    result = set()
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            result.add(d)
            n /= d
        else:
            d += 1
    if n > 1:
        result.add(n)
    return result


def count_find_num(primesL: list, limit: int) -> list:
    """
    Возврашает кол-во найденных чисел в интервале до limit, имеющих простые делители primesL
    :param primesL: list - Простые делители числа
    :param limit: int - Верхняя граница интервала поиска
    :return: list - кол-во найденных чисел и максимальное найденное число
    """
    numbers = []
    for number in range(2, limit + 1):
        if list(get_prime_divisors(number)) == primesL:
            numbers.append(number)
    return [len(numbers), max(numbers)] if len(numbers) > 0 else []


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
