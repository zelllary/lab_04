import csv
from pathlib import Path

import pytest

from algorithms.benchmark import benchmark_sort, measure_sort, run_benchmarks


def test_measure_and_repeats() -> None:
    """Тест замеров, повторов, копирования списка и ошибки числа повторов"""

    mas: list[int | float] = [3, 1.5, 2]
    received: list[list[int | float]] = []

    def sort_for_test(data: list[int | float]) -> list[int | float]:
        """Сортировка на месте для проверки копирования списка"""

        received.append(data.copy())
        data.sort()
        return data

    seconds = measure_sort(sort_for_test, mas)
    assert isinstance(seconds, float) and seconds >= 0
    assert received == [[3, 1.5, 2]]
    assert mas == [3, 1.5, 2]

    for repeats in (5, 7):
        received.clear()
        times = benchmark_sort(sort_for_test, mas, repeats)

        assert len(times) == repeats
        assert all(isinstance(time, float) and time >= 0 for time in times)
        assert received == [[3, 1.5, 2]] * repeats
        assert mas == [3, 1.5, 2]

    with pytest.raises(ValueError):
        benchmark_sort(sort_for_test, mas, repeats=4)

    assert len(received) == 7


def test_run_benchmarks_csv(tmp_path: Path) -> None:
    """Тест заголовков и записи всех сортировок, наборов и повторов в CSV"""

    file_name = tmp_path / "benchmark.csv"
    sizes = (0, 10)

    run_benchmarks(sizes, seed=42, file_name=str(file_name))

    with open(file_name, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == ["sorting", "dataset", "size", "repeat", "seconds"]
        rows = list(reader)

    assert len(rows) == 100
    assert all(float(row["seconds"]) >= 0 for row in rows)

    for sort_name in ("insertion", "quick"):
        for dataset in ("random", "sorted", "reverse", "nearly_sorted", "duplicates"):
            for size in sizes:
                group = [
                    row for row in rows
                    if row["sorting"] == sort_name
                    and row["dataset"] == dataset
                    and int(row["size"]) == size
                ]
                assert [int(row["repeat"]) for row in group] == [1, 2, 3, 4, 5]
