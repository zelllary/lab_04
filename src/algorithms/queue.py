class Queue:
    """Класс очереди"""

    def __init__(self) -> None:
        """Инициализация пустой очереди"""
        self.queue: list[object] = []
        self.head = 0

    def queue_add(self, value: object) -> None:
        """Добавление элемента в конец очереди"""

        self.queue.append(value)

    def __len__(self) -> int:
        """Длина очереди"""

        return len(self.queue) - self.head

    def __bool__(self) -> bool:
        """Проверка пустоты очереди"""

        return len(self) > 0

    def queue_peek(self) -> object:
        """Получение первого элемента в очереди
        Если она пуста - IndexError"""
        # вызывается __bool__
        if self:
            return self.queue[self.head]

        raise IndexError("Очередь пуста")

    def queue_pop(self) -> object:
        """Удаление первого элемента из очереди и его возвращение
        Если она пустая то - IndexError
        Если больше половины уже "освобождено" - сдвигаем список"""

        if not self:
            raise IndexError("Очередь пуста")

        element = self.queue[self.head]
        self.head += 1

        # если индекс первого элемента достиг середины и более - сдвигаем список
        if self.head * 2 >= len(self.queue):
            self.queue = self.queue[self.head : ]
            self.head = 0

        return element