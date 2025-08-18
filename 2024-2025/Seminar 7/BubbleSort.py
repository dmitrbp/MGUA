def swap(a, b):
    if a > b:
        a, b = b, a
    return a, b

def bubble_sort(a):
    n = len(a)
    swaped = False
    for i in range(1, n):
        for j in range(n - i):
            a[j], a[j + 1] = swap(a[j], a[j + 1])
            swaped = True  # Для того, чтобы выйти из внешнего цикла, если массив не изменился
            # if a[j] > a[j + 1]:
            #     a[j], a[j + 1] = a[j + 1], a[j]
        if not swaped:
            break

sorted_array = [4,3,6,1,5,2]
bubble_sort(sorted_array)
print(sorted_array)