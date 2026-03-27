def cocktail_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True
    step = 1

    while swapped:
        swapped = False

        # Проход слева направо (как в пузырьковой)
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        right -= 1  # Сужаем правую границу
        print(f"step {step}: {arr}") if swapped else None
        step += 1

        # Проход справа налево
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1  # Сужаем левую границу
        print(f"step {step}: {arr}") if swapped else None
        step += 1

arr = [ 2, 5, 6, 3, 8, 1, 4, 7]
print(arr)
cocktail_sort(arr)
print(arr)