def heapify(arr, n, i):
    """
    Преобразует поддерево с корнем i в max-heap.
    n - размер кучи, i - индекс корня поддерева
    """
    largest = i  # Инициализируем наибольший как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок существует и больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно преобразуем затронутое поддерево
        heapify(arr, n, largest)


def heapsort(arr):
    """Пирамидальная сортировка"""
    n = len(arr)

    # Построение max-heap (перестраиваем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        arr[0], arr[i] = arr[i], arr[0]

        # Восстанавливаем кучу для уменьшенного размера
        heapify(arr, i, 0)

    return arr


# Пример использования
my_list = [4, 10, 3, 5, 1, 8, 7, 2, 6, 9]
heapsort(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]