import pytest

from algorithms.algs import nested_structures_iterative, nested_structures_recursion


def test_nested_structures_recursion() -> None:
    """Тест обход вложенной структуры рекурсивно"""

    # создаем тестовую структуру
    test_list: list[int | str | list | set | tuple] = [1, (2, [3, "a"]), {4, 5}, (), 0]
    # вызываем функцию
    res = nested_structures_recursion(test_list)
    # проверяем через in так как порядок элементов в множестве не фиксирован
    assert res in (
        [1, 2, 3, "a", 4, 5, 0],
        [1, 2, 3, "a", 5, 4, 0],
    )

def test_nested_structures_recursion_destroy() -> None:
    """Тест обход вложенной структуры рекурсивно
      с неизвестным типом входных данных"""

    test = 67
    with pytest.raises(TypeError):
        nested_structures_recursion(test) # type: ignore[arg-type]

    test_list = [1, (2, [3, "a"]), {}, 0]
    with pytest.raises(TypeError):
        nested_structures_recursion(test_list) # type: ignore[arg-type]

def test_nested_structures_iterative() -> None:
    """Тест обход вложенной структуры итеративно"""

    # создаем тестовую структуру
    test_list: list[int | str | list | set | tuple] = [1, (2, [3, "a"]), {4, 5}, (), 0]
    # вызываем функцию
    res = nested_structures_iterative(test_list)
    # проверяем
    assert res in (
        [1, 2, 3, "a", 4, 5, 0],
        [1, 2, 3, "a", 5, 4, 0],
    )

def test_nested_structures_iterative_destroy() -> None:
    """Тест обход вложенной структуры итеративно
      с неизвестным типом входных данных"""

    test = 52
    with pytest.raises(TypeError):
        nested_structures_iterative(test) # type: ignore[arg-type]

    test_list = [1, (2, [3, "a"]), {}, 0]
    with pytest.raises(TypeError):
        nested_structures_iterative(test_list) # type: ignore[arg-type]

def test_nested_structures_empty_list() -> None:
    """Тест обход пустой вложеной структуры"""

    test_list: list[int | str | list | set | tuple] = []

    res1 = nested_structures_recursion(test_list)
    res2 = nested_structures_iterative(test_list)

    assert res1 == []
    assert res2 == []
