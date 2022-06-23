def bananas(s: str, word="banana", base="") -> set:
    """
    Возвращает количество слов «banana» в строке.
    :param word: str - Правильное слово
    :param s: str - Исходная строка
    :return: set - Комбинации строк без лишних символов
    """
    result = set()
    if not s and word:
        return result

    if not word:
        result = {base + "-" * len(s)}
        return result

    if s[0] != word[0]:
        result = bananas(s[1:], word, base + "-")
        return result
    result = bananas(s[1:], word[1:], base + word[0]).union(bananas(s[1:], word, base + "-"))
    return result


def test():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


if __name__ == '__main__':
    test()
