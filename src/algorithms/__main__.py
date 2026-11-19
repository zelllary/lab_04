from algorithms.algs import nested_structures_iterative, nested_structures_recursion
from algorithms.benchmark import run_benchmarks
from algorithms.generators import (
    generate_duplicates,
    generate_nearly_sorted,
    generate_random,
    generate_reverse,
    generate_sorted,
)
from algorithms.queue import Queue
from algorithms.sorting import insertion_sort, quick_sort


def main() -> None:
    """Примеры работы и замеры времени"""

    structure: list[int | str | list | set | tuple] = [1, (2, [3, "a"]), {4, 5}, (), 0]
    print("Рекурсивно:", nested_structures_recursion(structure))
    print("Итеративно:", nested_structures_iterative(structure))

    size = 10
    seed = 67
    mas = generate_random(size, seed)
    print("\nСлучайный список:", mas)
    print("Отсортированный:", generate_sorted(size))
    print("Обратный:", generate_reverse(size))
    print("Почти отсортированный:", generate_nearly_sorted(size, seed))
    print("С дубликатами:", generate_duplicates(size, seed))

    print("\nВставки:", insertion_sort(mas))
    print("Быстрая сортировка:", quick_sort(mas))
    print("Исходный список:", mas)

    queue = Queue()
    for value in (10, 2.5, "a"):
        queue.queue_add(value)

    print("\nДлина очереди:", len(queue))
    print("Есть элементы:", bool(queue))
    print("Первый элемент:", queue.queue_peek())
    while queue:
        print("Извлекли:", queue.queue_pop())
    print("Длина:", len(queue))
    print("Есть элементы:", bool(queue))

    try:
        queue.queue_pop()
    except IndexError as error:
        print(error)

    sizes = (1000, 3000, 10000)
    file_name = "benchmark_check.csv"
    print("\nЗамеры для размеров:", sizes)
    run_benchmarks(sizes, seed, file_name)
    print("Результаты в", file_name)


if __name__ == "__main__":
    main()
