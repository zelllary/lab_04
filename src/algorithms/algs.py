def nested_structures_recursion(structure: 
                      list[int | str | list | set | tuple] | 
                      set[int | str | list | set | tuple] | 
                      tuple[int | str | list | set | tuple, ...]
                      ) -> list[int | str]:
    """Обход вложенных структур рекурсивно"""

    if type(structure) not in [list, set, tuple]:
        raise TypeError('Неизвестный тип данных в вложенной структуре')
    res = []
    
    # идем по структуре 
    for element in structure:
        # если элемент структура
        if (isinstance(element, (list, tuple, set))):
            res.extend(nested_structures_recursion(element))
        # если элемент число или строка
        elif (isinstance(element, (int, str))):
            res.append(element)
        # неизвестный тип данных
        else:
            raise TypeError('Неизвестный тип данных в вложенной структуре')

    return res

def nested_structures_iterative(structure: 
                      list[int | str | list | set | tuple] | 
                      set[int | str | list | set | tuple] | 
                      tuple[int | str | list | set | tuple, ...]
                      ) -> list[int | str]:
    """Обход вложенных структур итеративно"""

    if type(structure) not in [list, set, tuple]:
        raise TypeError('Неизвестный тип данных в вложенной структуре')
    res: list[int | str] = []
    # кладем структуру в стек
    stack: list[int | str | list | set | tuple] = [structure]
    # идем по стеку пока он не станет пуст
    while(stack):
        # берем последний элемент
        current = stack.pop()
        # если элемент список\множество\кортеж
        if (isinstance(current, (list, set, tuple))):
            # превращаем структуру в список, переворачиваем и добавляем в стек
            items = reversed(list(current))
            # добавляем в стек в обратном порядке
            stack.extend(items)
        elif isinstance(current, (int, str)):
            res.append(current)
        else:
            raise TypeError('Неизвестный тип данных в вложенной структуре')

    return res



