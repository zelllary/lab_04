import csv
from pathlib import Path

from algorithms.benchmark import create_report
from algorithms.sorting import insertion_sort


def test_insertion_sort_stability() -> None:
    """Тест сохранения порядка элементов с одинаковым значением"""

    test_list: list[int | float] = [2.0, 1, 2, 1.0]
    res = insertion_sort(test_list)

    assert res == [1, 1.0, 2.0, 2]
    # проверяем типы, потому что 1 и 1.0 равны по значению
    assert [type(value) for value in res] == [int, float, float, int]


def test_create_report(tmp_path: Path) -> None:
    """Тест создания отчёта"""

    # файлы для теста
    file_name = tmp_path / "benchmark.csv"
    report_name = tmp_path / "report.md"

    # записываем несколько замеров
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["sorting", "dataset", "size", "repeat", "seconds"])
        writer.writerows([
            ["quick", "random", 20, 1, 0.6],
            ["quick", "random", 10, 1, 0.1],
            ["quick", "random", 10, 2, 0.3],
            ["quick", "sorted", 10, 1, 0.05],
            ["insertion", "random", 10, 1, 0.0],
            ["insertion", "random", 20, 1, 0.4],
        ])

    # создаем отчет и читаем его
    create_report(str(file_name), str(report_name))
    report = report_name.read_text(encoding="utf-8")

    # проверяем среднее время и рост
    assert "| quick | random | 10 | 2 | 0.2 | - |" in report
    assert "| quick | random | 20 | 1 | 0.6 | 3.0 |" in report
    # другой набор считается отдельно
    assert "| quick | sorted | 10 | 1 | 0.05 | - |" in report
    # если прошлое время нулевое, рост не считаем
    assert "| insertion | random | 20 | 1 | 0.4 | - |" in report
