from random import Random


def generate_random(size: int, seed: int | None = None) -> list[int | float]:
    """Генератор случайного списка с целыми и вещественными числами"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    # задаем начальное значение генератора
    generator = Random(seed)

    res: list[int | float] = []
    # генерируем size чисел
    for i in range(size):
        if i % 2 == 0:
            res.append(generator.randint(-size, size))
        else:
            res.append(round(generator.uniform(-size, size), 1))

    return res

def generate_sorted(size: int) -> list[int | float]:
    """Генерация отсортированного по возрастанию списка"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    res: list[int | float] = [
        i if i % 2 == 0 else i + 0.5
        for i in range(size)
    ]

    return res

def generate_reverse(size: int) -> list[int | float]:
    """Генерация списка отсортированного по убыванию"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    res: list[int | float] = [
        i if i % 2 == 0 else i + 0.5
        for i in range(size - 1, -1, -1)
    ]

    return res

def generate_nearly_sorted(size: int, seed: int | None = None) -> list[int | float]:
    """Генерация почти отсортированного списка"""

    res: list[int | float] = generate_sorted(size)

    if len(res) < 2:
        return res
    # создаем генератор на индексы для обмена
    generator = Random(seed)
    # выбираем количество обменов
    swaps = max(1, size // 100)

    for i in range(swaps):
        # выбираем индексы
        first = generator.randint(0, size - 1)
        second = generator.randint(0, size - 1)
        # проверяем чтобы индексы не совпадали
        while first == second:
            second = generator.randint(0, size - 1)
        # меняем местами
        res[first], res[second] = res[second], res[first]

    return res

def generate_duplicates(size: int, seed: int | None = None) -> list[int | float]:
    """Генерация списка с дубликатами"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    generator = Random(seed)

    res: list[int | float] = []

    for i in range(size):
        res.append(generator.choice((0, 1.5, 2, 3.5, 4)))

    return res

