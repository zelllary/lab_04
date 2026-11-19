from random import Random


def generate_random(size: int, seed: int | None = None) -> list[int | float]:
    """Генератор случайного списка"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError
    
    # задаем начальное значение генератора
    generator = Random(seed)

    res: list[int | float] = []
    # генерируем size чисел
    for i in range(size):
        res.append(generator.randint(-size, size))

    return res

def generate_sorted(size: int) -> list[int]:
    """Генерация отсортированного по возрастанию списка"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    res: list[int] = list(range(size))

    return res

def generate_reverse(size: int) -> list[int]:
    """Генерация списка отсортированного по убыванию"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    res: list[int] = list(range(size - 1, -1, -1))

    return res

def generate_nearly_sorted(size: int, seed: int | None = None) -> list[int]:
    """Генерация почти отсортированного списка"""

    res: list[int] =  generate_sorted(size)

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

def generate_duplicates(size: int, seed: int | None = None) -> list[int]:
    """Генерация списка с дубликатами"""

    # размер не может быть отрицательным
    if size < 0:
        raise ValueError

    generator = Random(seed)

    res: list[int] = []

    for i in range(size):
        res.append(generator.randint(0,4))

    return res
    