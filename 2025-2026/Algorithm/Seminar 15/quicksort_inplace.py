def quicksort_inplace(arr, low=0, high=None):
    """Быстрая сортировка на месте"""
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Разделяем и получаем индекс опорного элемента
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем левую и правую части
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    """
    Разделение массива относительно опорного элемента.
    Возвращает индекс опорного элемента после разделения.
    """
    # Выбираем последний элемент как опорный
    pivot = arr[high]
    i = low - 1  # Индекс меньшего элемента

    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Ставим опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Пример
my_list = [8, 3, 9, 2, 7, 1, 5, 6, 4]
quicksort_inplace(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]