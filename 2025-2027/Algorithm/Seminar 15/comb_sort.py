def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    shrink = 1.247  # Фактор уменьшения

    while gap > 1 or swapped:
        # Обновляем gap
        gap = max(1, int(gap / shrink))

        swapped = False

        # Один проход с текущим gap
        for i in range(n - gap):
            print("gap=", gap, "arr[i]=", arr[i], "arr[i+gap]=", arr[i + gap], "list=", my_list)
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                print("!gap=", gap, "arr[i]=", arr[i], "arr[i+gap]=", arr[i + gap], "list=", my_list)
                swapped = True


# Пример использования
my_list = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
comb_sort(my_list)
print(my_list)  # [-44, -6, 0, 1, 3, 4, 8, 23, 28, 56]