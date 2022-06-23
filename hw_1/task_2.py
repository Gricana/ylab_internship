def int32_to_ip(int32: int) -> str:
    """
    :param int32: int - 32-битное число
    :return: str - Строку, являющуюся 4-х битным IP
    """
    return '.'.join([str((int32 >> 8 * i) % 256) for i in range(3, -1, -1)])


def test():
    """"
    Тесты на проверку правильности выполнения функции int32_to_ip
    :return: None
    """
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


if __name__ == '__main__':
    print(int32_to_ip(32))
    test()
