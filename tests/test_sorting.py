from collections.abc import Callable
from random import Random

import pytest

from algorithms.sorting import insertion_sort, quick_sort


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки без изменения исходного списка"""

    test_list: list[int | float] = [5, -2.5, 3, 0.0, -2.5, 1]
    original_list = test_list.copy()
    res = sort_function(test_list)

    assert res == [-2.5, -2.5, 0.0, 1, 3, 5]
    assert test_list == original_list
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_empty_list(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки пустого списка"""

    test_list: list[int | float] = []
    res = sort_function(test_list)

    assert res == []
    assert test_list == []
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_single_element(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки списка из одного элемента"""

    test_list: list[int | float] = [7.5]
    res = sort_function(test_list)

    assert res == [7.5]
    assert test_list == [7.5]
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_sorted_list(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки уже отсортированного списка"""

    test_list: list[int | float] = [-5.5, -1, 0.0, 2, 8.25]
    original_list = test_list.copy()
    res = sort_function(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_reversed_list(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки списка в обратном порядке"""

    test_list: list[int | float] = [8.25, 2, 0.0, -1, -5.5]
    original_list = test_list.copy()
    res = sort_function(test_list)

    assert res == [-5.5, -1, 0.0, 2, 8.25]
    assert test_list == original_list
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_duplicates(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки списка с дубликатами"""

    test_list: list[int | float] = [3, 1.5, 3, 2, 1.5, 2]
    original_list = test_list.copy()
    res = sort_function(test_list)

    assert res == [1.5, 1.5, 2, 2, 3, 3]
    assert test_list == original_list
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_negative_numbers(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест сортировки отрицательных чисел"""

    test_list: list[int | float] = [-4.5, -1, -7.25, -3]
    original_list = test_list.copy()
    res = sort_function(test_list)

    assert res == [-7.25, -4.5, -3, -1]
    assert test_list == original_list
    assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_random_lists(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест совпадения сортировки случайных списков с эталоном"""

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
            res = sort_function(test_list)

            assert res == sorted(original_list)
            assert test_list == original_list
            assert res is not test_list


@pytest.mark.parametrize("sort_function", [insertion_sort, quick_sort])
def test_sort_invalid_types(sort_function: Callable[[list[int | float]], list[int | float]]) -> None:
    """Тест ошибок типов входного списка и его элементов"""

    test = 42
    with pytest.raises(TypeError):
        sort_function(test)  # type: ignore[arg-type]

    test_list: list[int | float | str] = [1, "a", 2.5]
    with pytest.raises(TypeError):
        sort_function(test_list)  # type: ignore[arg-type]
