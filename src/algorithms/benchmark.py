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


