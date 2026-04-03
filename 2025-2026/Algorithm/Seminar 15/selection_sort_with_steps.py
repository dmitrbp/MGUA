def selection_sort_with_steps(arr):
    n = len(arr)
    print(f"Начальный массив: {arr}")

    for i in range(n):
        min_idx = i
        print(f"\nШаг {i + 1}:")
        print(f"  Ищем минимум в [{i}:{n}] = {arr[i:]}")

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"    Новый минимум: {arr[min_idx]} на позиции {min_idx}")

        if min_idx != i:
            print(f"  Меняем {arr[i]} и {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"  Элемент {arr[i]} уже на своем месте")

        print(f"  Результат: {arr}")

    return arr


# Пример
my_list = [29, 10, 14, 37, 13]
selection_sort_with_steps(my_list)