def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)

    # Базовый случай: один элемент уже отсортирован
    if n <= 1:
        return

    # Сортируем первые n-1 элементов
    insertion_sort_recursive(arr, n - 1)

    # Вставляем последний элемент в отсортированную часть
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


# Пример использования
my_list = [5, 2, 4, 6, 1, 3]
insertion_sort_recursive(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6]