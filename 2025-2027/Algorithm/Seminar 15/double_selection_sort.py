def double_selection_sort(arr):
    n = len(arr)

    for i in range(n // 2):
        min_idx = i
        max_idx = i

        # Ищем одновременно минимум и максимум
        for j in range(i + 1, n - i):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j

        # Ставим минимум в начало
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Если максимум был на позиции i, его индекс изменился
        if max_idx == i:
            max_idx = min_idx

        # Ставим максимум в конец
        if max_idx != n - 1 - i:
            arr[n - 1 - i], arr[max_idx] = arr[max_idx], arr[n - 1 - i]


# Пример
my_list = [64, 25, 12, 22, 11, 90, 5, 33]
double_selection_sort(my_list)
print(my_list)  # [5, 11, 12, 22, 25, 33, 64, 90]