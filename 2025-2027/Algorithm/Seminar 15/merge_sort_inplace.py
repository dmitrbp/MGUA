def merge_sort_inplace(arr, left=0, right=None):
    """Сортировка слиянием с работой на исходном массиве"""
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2

        # Сортируем левую и правую половины
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)

        # Сливаем в буфер
        merge_inplace(arr, left, mid, right)


def merge_inplace(arr, left, mid, right):
    """Слияние двух отсортированных частей массива"""
    # Создаем копии левой и правой частей
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    # Сливаем обратно в исходный массив
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Копируем остатки
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# Пример
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort_inplace(my_list)
print(my_list)  # [3, 9, 10, 27, 38, 43, 82]