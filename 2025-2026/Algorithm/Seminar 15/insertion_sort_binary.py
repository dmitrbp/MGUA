import bisect

def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Находим позицию для вставки с помощью бинарного поиска
        pos = bisect.bisect_left(arr, key, 0, i)
        # Сдвигаем элементы
        arr[pos + 1:i + 1] = arr[pos:i]
        arr[pos] = key


def insertion_sort_binary_manual(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i

        # Бинарный поиск позиции для вставки
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid
            else:
                left = mid + 1

        # Сдвигаем элементы
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key


# Пример использования
my_list = [5, 2, 4, 6, 1, 3]
insertion_sort_binary(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6]

my_list = [5, 2, 4, 6, 1, 3]
insertion_sort_binary_manual(my_list)
print(my_list)  # [1, 2, 3, 4, 5, 6]