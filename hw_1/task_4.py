from itertools import combinations


def bananas(s: str, word="banana") -> set:
    """
    Возвращает комбинации слов с убранными лишними символами
    :param s: Исходное слово с лишними символами
    :param word: Правильное слово
    :return: set - Комбинации слов, где лишние символы заменены на "-" (дефис)
    """
    result: set = set()
    len_s: int = len(s)

    for indexes in combinations(range(len_s), len_s - 6):
        symbols = list(s)

        for i in indexes:
            symbols[i] = '-'

        temp_str = ''.join(symbols)

        if temp_str.replace('-', '') == word:
            result.add(temp_str)

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
