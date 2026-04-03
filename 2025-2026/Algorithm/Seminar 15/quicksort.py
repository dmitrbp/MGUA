def quicksort(arr):
    """Быстрая сортировка (создает новый массив)"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Опорный элемент (середина)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Пример использования
my_list = [8, 3, 9, 2, 7, 1, 5, 6, 4]
sorted_list = quicksort(my_list)
print(sorted_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]