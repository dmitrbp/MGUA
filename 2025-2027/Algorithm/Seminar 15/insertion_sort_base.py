def insertion_sort_base(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1  # Начинаем с предыдущего элемента

        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем key на правильную позицию
        arr[j + 1] = key
        print("i=", i, "arr=", arr)


# Пример использования
my_list = [2, 5, 3, 6, 8, 1, 4, 7]
print(my_list)
insertion_sort_base(my_list)
print(my_list)