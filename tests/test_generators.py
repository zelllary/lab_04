import pytest

from algorithms.generators import (
    generate_duplicates,
    generate_nearly_sorted,
    generate_random,
    generate_reverse,
    generate_sorted,
)


def test_generate_random() -> None:
    """Тест размера, границ значений и воспроизводимости случайного списка"""

    res = generate_random(100, seed=42)

    assert len(res) == 100
    assert all(-100 <= value <= 100 for value in res)
    assert {type(value) for value in res} == {int, float}
    assert res == generate_random(100, seed=42)
    assert res != generate_random(100, seed=43)


def test_generate_sorted_and_reverse() -> None:
    """Тест списков по возрастанию и убыванию"""

    assert generate_sorted(5) == [0, 1.5, 2, 3.5, 4]
    assert generate_reverse(5) == [4, 3.5, 2, 1.5, 0]


def test_generate_nearly_sorted() -> None:
    """Тест сохранения чисел, небольшого числа перестановок и seed"""

    res = generate_nearly_sorted(1000, seed=42)
    original = generate_sorted(1000)
    changed = sum(value != original[index] for index, value in enumerate(res))

    assert sorted(res) == original
    assert 0 < changed <= 20
    assert res == generate_nearly_sorted(1000, seed=42)
    assert res != generate_nearly_sorted(1000, seed=43)
    assert generate_nearly_sorted(2, seed=42) == [1.5, 0]


def test_generate_duplicates() -> None:
    """Тест размера, повторов, диапазона значений и воспроизводимости"""

    res = generate_duplicates(100, seed=42)

    assert len(res) == 100
    assert set(res) <= {0, 1.5, 2, 3.5, 4}
    assert len(set(res)) < len(res)
    assert {type(value) for value in res} == {int, float}
    assert res == generate_duplicates(100, seed=42)
    assert res != generate_duplicates(100, seed=43)


def test_generators_empty_single_and_negative_size() -> None:
    """Тест пустого списка, одного элемента и ошибки отрицательного размера"""

    for generator in (
        generate_random,
        generate_sorted,
        generate_reverse,
        generate_nearly_sorted,
        generate_duplicates,
    ):
        assert generator(0) == []
        assert len(generator(1)) == 1

        with pytest.raises(ValueError):
            generator(-1)
