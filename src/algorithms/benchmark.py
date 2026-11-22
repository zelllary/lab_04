import csv
from collections.abc import Callable
from time import perf_counter

from algorithms.generators import (
    generate_duplicates,
    generate_nearly_sorted,
    generate_random,
    generate_reverse,
    generate_sorted,
)
from algorithms.sorting import insertion_sort, quick_sort


def measure_sort(
    sort_function: Callable[[list[int | float]], list[int | float]],
    data: list[int | float],
) -> float:
    """Замер времени работы функции"""

    data_copy = data.copy()
    # засекаем время начала
    start = perf_counter()
    # вызываем функцию
    sort_function(data_copy)
    # засекаем время конца
    end = perf_counter()

    return end - start

def benchmark_sort(
    sort_function: Callable[[list[int | float]], list[int | float]],
    data: list[int | float],
    repeats: int = 5,
) -> list[float]:
    """Запуск нескольких, но не менее 5 повторов"""

    if repeats < 5:
        raise ValueError("Не менее 5 повторений в benchmark_sort")

    times: list[float] = []

    for i in range(repeats):
        times.append(measure_sort(sort_function, data))

    return times

def run_benchmarks(sizes: tuple[int, ...], seed: int = 42, file_name: str = "output.csv") -> None:
    """Запуск замеров сортировок для разных размеров"""
    # словарь сортировок
    sorts = {
        "insertion": insertion_sort,
        "quick": quick_sort,
    }

    with open(file_name, "w", newline="", encoding="utf-8") as file:
        # создаем обьект записи и записываем заголовки
        writer = csv.writer(file)
        writer.writerow(["sorting", "dataset", "size", "repeat", "seconds"])

        # идем по размерам списков
        for size in sizes:
            for dataset_name in ("random", "sorted", "reverse", "nearly_sorted", "duplicates"):
                # генерируем список
                mas: list[int | float]
                if dataset_name == 'random':
                    mas = generate_random(size, seed)
                elif dataset_name == 'sorted':
                    mas  = generate_sorted(size)
                elif dataset_name == 'reverse':
                    mas = generate_reverse(size)
                elif dataset_name == 'nearly_sorted':
                    mas = generate_nearly_sorted(size, seed)
                else:
                    mas = generate_duplicates(size, seed)
                # перебираем сортировки
                for sort_name, sort_function in sorts.items():
                    # вызываем замер времени на нескольких повторах
                    times = benchmark_sort(sort_function, mas)
                    # перебираем номер повтора и их длительности
                    for repeat, seconds in enumerate(times, start=1):
                        # записываем результат одного замера
                        writer.writerow([sort_name, dataset_name, size, repeat, seconds])


def create_report(file_name: str, report_name: str = "benchmark_report.md") -> None:
    """Создание отчёта по замерам"""

    results: dict[tuple[str, str, int], list[float]] = {}

    # читаем замеры из csv
    with open(file_name, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            # собираем повторы одной сортировки, набора и размера
            key = (row["sorting"], row["dataset"], int(row["size"]))
            if key not in results:
                results[key] = []
            results[key].append(float(row["seconds"]))

    with open(report_name, "w", encoding="utf-8") as file:
        # записываем заголовок таблицы
        file.write("# Benchmark\n\n")
        file.write("| sorting | dataset | size | repeats | average_seconds | growth |\n")
        file.write("| --- | --- | ---: | ---: | ---: | ---: |\n")

        last_group = ("", "")
        last_time = 0.0

        # идем по сортировкам и наборам, размеры по возрастанию
        for key in sorted(results):
            sort_name, dataset, size = key
            times = results[key]
            # считаем среднее время повторов
            average = sum(times) / len(times)
            group = (sort_name, dataset)

            # сравниваем с предыдущим размером того же набора
            growth = "-"
            if group == last_group and last_time > 0:
                growth = str(round(average / last_time, 2))

            # записываем строку отчета
            file.write(
                f"| {sort_name} | {dataset} | {size} | {len(times)} | "
                f"{round(average, 6)} | {growth} |\n"
            )
            last_group = group
            last_time = average


