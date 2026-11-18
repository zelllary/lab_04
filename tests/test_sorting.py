from random import Random

import pytest

from algorithms.sorting import insertion_sort, quick_sort


def test_insertion_sort() -> None:
    """Тест сортировки вставками без изменения исходного списка"""

    test_list: list[int | float] = [5, -2.5, 3, 0.0, -2.5, 1]
    original_list = test_list.copy()
    res = insertion_sort(test_list)

    assert res == [-2.5, -2.5, 0.0, 1, 3, 5]
    assert test_list == original_list
    assert res is not test_list


def test_insertion_sort_empty_list() -> None:
    """Тест сортировки пустого списка"""

    test_list: list[int | float] = []
    res = insertion_sort(test_list)

    assert res == []
    assert test_list == []
    assert res is not test_list


def test_insertion_sort_single_element() -> None:
    """Тест сортировки списка из одного элемента"""

    test_list: list[int | float] = [7.5]
    res = insertion_sort(test_list)

    assert res == [7.5]
    assert test_list == [7.5]
    assert res is not test_list


def test_insertion_sort_sorted_list() -> None:
    """Тест сортировки вставками уже отсортированного списка"""

    test_list: list[int | float] = [-5.5, -1, 0.0, 2, 8.25]
    original_list = test_list.copy()
    res = insertion_sort(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


def test_insertion_sort_reversed_list() -> None:
    """Тест сортировки вставками списка в обратном порядке"""

    test_list: list[int | float] = [8.25, 2, 0.0, -1, -5.5]
    original_list = test_list.copy()
    res = insertion_sort(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


def test_insertion_sort_duplicates() -> None:
    """Тест сортировки вставками списка с дубликатами"""

    test_list: list[int | float] = [3, 1.5, 3, 2, 1.5, 2]
    original_list = test_list.copy()
    res = insertion_sort(test_list)

    assert res == [1.5, 1.5, 2, 2, 3, 3]
    assert test_list == original_list
    assert res is not test_list


def test_insertion_sort_negative_numbers() -> None:
    """Тест сортировки вставками отрицательных чисел"""

    test_list: list[int | float] = [-4.5, -1, -7.25, -3]
    original_list = test_list.copy()
    res = insertion_sort(test_list)

    assert res == [-7.25, -4.5, -3, -1]
    assert test_list == original_list
    assert res is not test_list


def test_insertion_sort_random_lists() -> None:
    """Тест совпадения сортировки вставками случайных списков с эталоном"""

    generator = Random(42)

    for size in (0, 1, 2, 10, 50, 100):
        for _ in range(5):
            test_list: list[int | float] = []
            for index in range(size):
                if index % 2 == 0:
                    test_list.append(generator.randint(-100, 100))
                else:
                    test_list.append(generator.uniform(-100, 100))
            original_list = test_list.copy()
            res = insertion_sort(test_list)

            assert res == sorted(original_list)
            assert test_list == original_list
            assert res is not test_list


def test_insertion_sort_invalid_types() -> None:
    """Тест ошибок типов входного списка и его элементов для вставок"""

    test = 42
    with pytest.raises(TypeError):
        insertion_sort(test)  # type: ignore[arg-type]

    test_list: list[int | float | str] = [1, "a", 2.5]
    with pytest.raises(TypeError):
        insertion_sort(test_list)  # type: ignore[arg-type]


def test_quick_sort_empty_list() -> None:
    """Тест быстрой сортировки пустого списка"""

    test_list: list[int | float] = []
    res = quick_sort(test_list)

    assert res == []
    assert test_list == []
    assert res is not test_list


def test_quick_sort_single_element() -> None:
    """Тест быстрой сортировки списка из одного элемента"""

    test_list: list[int | float] = [7.5]
    res = quick_sort(test_list)

    assert res == [7.5]
    assert test_list == [7.5]
    assert res is not test_list


def test_quick_sort_sorted_list() -> None:
    """Тест быстрой сортировки уже отсортированного списка"""

    test_list: list[int | float] = [-5.5, -1, 0.0, 2, 8.25]
    original_list = test_list.copy()
    res = quick_sort(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


def test_quick_sort_reversed_list() -> None:
    """Тест быстрой сортировки списка в обратном порядке"""

    test_list: list[int | float] = [8.25, 2, 0.0, -1, -5.5]
    original_list = test_list.copy()
    res = quick_sort(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


def test_quick_sort_duplicates() -> None:
    """Тест быстрой сортировки списка с дубликатами"""

    test_list: list[int | float] = [3, 1.5, 3, 2, 1.5, 2]
    original_list = test_list.copy()
    res = quick_sort(test_list)

    assert res == [1.5, 1.5, 2, 2, 3, 3]
    assert test_list == original_list
    assert res is not test_list


def test_quick_sort_negative_numbers() -> None:
    """Тест быстрой сортировки отрицательных чисел"""

    test_list: list[int | float] = [-4.5, -1, -7.25, -3]
    original_list = test_list.copy()
    res = quick_sort(test_list)

    assert res == [-7.25, -4.5, -3, -1]
    assert test_list == original_list
    assert res is not test_list


def test_quick_sort_random_lists() -> None:
    """Тест совпадения быстрой сортировки случайных списков с эталоном"""

    generator = Random(42)

    for size in (0, 1, 2, 10, 50, 100):
        for _ in range(5):
            test_list: list[int | float] = []
            for index in range(size):
                if index % 2 == 0:
                    test_list.append(generator.randint(-100, 100))
                else:
                    test_list.append(generator.uniform(-100, 100))
            original_list = test_list.copy()
            res = quick_sort(test_list)

            assert res == sorted(original_list)
            assert test_list == original_list
            assert res is not test_list


def test_quick_sort_invalid_types() -> None:
    """Тест ошибок типов входного списка и его элементов для quicksort"""

    test = 42
    with pytest.raises(TypeError):
        quick_sort(test)  # type: ignore[arg-type]

    test_list: list[int | float | str] = [1, "a", 2.5]
    with pytest.raises(TypeError):
        quick_sort(test_list)  # type: ignore[arg-type]
