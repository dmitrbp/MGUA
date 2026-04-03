def heapify_iterative(arr, n, i):
    """Итеративная версия heapify (избегает рекурсии)"""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest  # Продолжаем с позиции largest


def heapsort_iterative(arr):
    """Пирамидальная сортировка с итеративным heapify"""
    n = len(arr)

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify_iterative(arr, n, i)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_iterative(arr, i, 0)

    return arr


# Пример
my_list = [4, 10, 3, 5, 1, 8, 7, 2, 6, 9]
heapsort_iterative(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]