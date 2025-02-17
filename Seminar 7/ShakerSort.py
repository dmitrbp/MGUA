def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    swapped = True
    step = 1
    while left < right and swapped:
        swapped = False
        # Проход слева направо
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        right -= 1
        print(f'step {step} - {arr}') if swapped else None
        step += 1
        # Проход справа налево
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        left += 1
        print(f'step {step} - {arr}') if swapped else None
        step += 1
    return arr


arr = [4, 3, 6, 1, 5, 2]
print(f'Unsorted - {arr}')
sorted_arr = shaker_sort(arr)
print(f'Sorted - {sorted_arr}')
