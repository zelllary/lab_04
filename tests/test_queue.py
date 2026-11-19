import pytest

from algorithms.queue import Queue


def test_queue_empty() -> None:
    """Тест длины, пустоты и ошибок операций над пустой очередью"""

    queue = Queue()

    assert len(queue) == 0
    assert not queue

    with pytest.raises(IndexError):
        queue.queue_peek()

    with pytest.raises(IndexError):
        queue.queue_pop()


def test_queue_fifo_invariant() -> None:
    """Тест сохранения порядка FIFO при чередовании добавления и извлечения"""

    queue = Queue()
    for value in (10, 20, 30):
        queue.queue_add(value)

    for added, removed in ((40, 10), (50, 20), (60, 30)):
        assert queue.queue_pop() == removed
        queue.queue_add(added)
        assert len(queue) == 3

    res = [queue.queue_pop() for _ in range(3)]
    assert res == [40, 50, 60]
    assert not queue


def test_queue_peek() -> None:
    """Тест просмотра первого элемента без изменения очереди"""

    queue = Queue()
    for value in (10, 20, 30):
        queue.queue_add(value)

    assert queue.queue_peek() == 10
    assert len(queue) == 3

    queue.queue_pop()
    assert queue.queue_peek() == 20
    assert len(queue) == 2

    res = [queue.queue_pop() for _ in range(2)]
    assert res == [20, 30]


def test_queue_cleanup() -> None:
    """Тест очистки обработанной части списка с сохранением элементов очереди"""

    queue = Queue()
    for value in (10, 20, 30, 40, 50, 60):
        queue.queue_add(value)

    queue.queue_pop()
    queue.queue_pop()
    assert queue.head == 2

    queue.queue_pop()
    assert queue.head == 0
    assert queue.queue == [40, 50, 60]
    assert len(queue) == 3

    res = [queue.queue_pop() for _ in range(3)]
    assert res == [40, 50, 60]
    assert queue.queue == []
    assert queue.head == 0


def test_queue_reuse() -> None:
    """Тест одного элемента и повторного использования опустошённой очереди"""

    queue = Queue()
    for value in (0, None, "sixseven", 6.7):
        queue.queue_add(value)

        assert len(queue) == 1
        assert queue
        assert queue.queue_peek() == value
        assert queue.queue_pop() == value
        assert not queue
