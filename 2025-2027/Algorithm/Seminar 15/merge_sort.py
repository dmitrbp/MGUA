def merge_sort(arr):
    """Рекурсивная сортировка слиянием"""
    if len(arr) <= 1:
        return arr

    # Разделяем массив пополам
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем обе половины
    left = merge_sort(left)
    right = merge_sort(right)

    # Сливаем отсортированные половины
    return merge(left, right)


def merge(left, right):
    """Слияние двух отсортированных массивов"""
    result = []
    i = j = 0

    # Сравниваем элементы и добавляем меньший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Пример использования
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(sorted_list)  # [3, 9, 10, 27, 38, 43, 82]