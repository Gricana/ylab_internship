import re


def domain_name(url: str) -> str:
    """
    Функция для нахождения домена нижнего уровня из URL
    :param url: Полный URL страницы
    :return: Домен нижнего уровня
    """
    pattern: str = r"[^htpsw\./]+[\w-]+"
    return re.search(pattern, url)[0]


def test():
    """
    Тесты на проверку правильности выполнения функции domain_name
    :return: None
    """
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


if __name__ == '__main__':
    test()
