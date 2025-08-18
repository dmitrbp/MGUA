def bubble_sort_recursive(a, iter = 0):
    print(f'Enter to iteration {iter}')
    n = len(a)
    swaped = False
    for i in range(n - 1 - iter):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaped = True
    iter += 1
    bubble_sort_recursive(a, iter) if swaped and iter < n - 1 else None
    print(f'Exiting from iteration {iter - 1}')


sorted_array = [4, 3, 6, 1, 5, 2, 7, 1, 0]
# sorted_array = [1, 2, 3, 4, 5, 6, 7,]
bubble_sort_recursive(sorted_array)
print(sorted_array)
