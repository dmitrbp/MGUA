def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Находим индекс минимального элемента в неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Меняем местами текущий элемент с найденным минимумом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort_desc(arr):
    n = len(arr)

    for i in range(n):
        # Находим индекс максимального элемента
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        # Меняем местами
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


# Пример использования
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print(my_list)  # [11, 12, 22, 25, 64]

# Пример
my_list = [64, 25, 12, 22, 11]
selection_sort_desc(my_list)
print(my_list)  # [64, 25, 22, 12, 11]