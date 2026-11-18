def insertion_sort(mas:list[int | float]) -> list[int | float]:
    """Сортировка вставками (возвращает новый список, не меняя исходный)
    если неверный тип данных или сравнение несовместимых элементов - TypeError"""

    if not isinstance(mas, list):
        raise TypeError('Неверный тип данных для сортировки')
    
    mas_copy = mas.copy()

    # идем по массиву, начиная со 2го элемента
    for i in range(1, len(mas_copy)):
        # индекс предыдущего элемента относительно текущего
        j = i - 1
        current = mas_copy[i]
        # пока мы можем идти влево и пока текущий элемент меньше того на котором стоим
        while j >= 0 and mas_copy[j] > current:
            # копируем этот элемент в следующую соседнюю ячейку (сдвигаем вправо) 
            mas_copy[j + 1] = mas_copy[j]
            j -= 1
        # записываем текущий элемент на его место
        mas_copy[j+1] = current

    return mas_copy

def quick_sort(mas: list[int | float]) -> list[int | float]:
    """Быстрая сортировка (возвращает новый список, не меняя исходный)
    если неверный тип данных или сравнение несовместимых элементов - TypeError"""

    if not isinstance(mas, list):
        raise TypeError('Неверный тип данных для сортировки')
    
    mas_copy = mas.copy()

    # списки длины 0 или 1 уже отсортированы
    if len(mas_copy) < 2:
        return mas_copy
    
    # стек участков которые нужно обработать
    stack = [(0, len(mas_copy) - 1)]

    while stack:
        # получаем границы очередного участка
        left, right = stack.pop()
        # опорное значение
        middle = mas_copy[(left+right)//2]
        less = left      # позиция следующего элемента меньше опорного
        current = left   # индекс проверяемого сейчас элемента
        untested = right # последний индекс ещё не проверенной области

        # пока непроверенная область есть
        while current <= untested:
            # если текущий элемент меньше опорного
            if mas_copy[current] < middle:
                # меняем местами текущий элемент и элемент на позиции less
                mas_copy[current], mas_copy[less] = mas_copy[less], mas_copy[current]
                # увеличиваем индексы
                current += 1
                less += 1
            # больше
            elif mas_copy[current] > middle:
                # меняем текущий элемент с последним непроверенным
                mas_copy[current], mas_copy[untested] = mas_copy[untested], mas_copy[current]
                # уменьшаем непроверенную область
                untested -= 1
            # равны
            else:
                current +=1
        # проверяем длину левого участка (меньше опорного)
        if less - left > 1:
            stack.append((left, less - 1))
        # проверяем длину правого участка (больше опорного)
        if right - untested > 1:
            stack.append((untested + 1, right))

    return mas_copy
        


    

