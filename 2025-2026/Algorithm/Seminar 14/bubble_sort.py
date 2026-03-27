import time

RED = '\033[31m'
RESET = '\033[0m'

def bubble_sort(arr):
    print_arr(arr)
    time.sleep(2)
    n = len(arr)
    step = 0
    # Проходим по массиву n-1 раз
    for i in range(n - 1):
        # Последние i элементов уже на своих местах
        for j in range(n - i - 1):
            is_swap = False
            if arr[j] > arr[j + 1]:
                # Меняем местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap = True
            step += 1
            print_arr(arr, j + 1, is_swap, step)
            time.sleep(2)
    return arr

def print_arr(arr, j = 0, is_swap = False, step = 0):
    s = ''
    for i in range(len(arr)):
        if is_swap and i == j:
            s += " " + RED + str(arr[i]) + RESET
        else:
            s += " " + str(arr[i])

    print(f"\rstep {step}: {s}", end='')

bubble_sort([0, 5, 4, 3, 2, 1])
