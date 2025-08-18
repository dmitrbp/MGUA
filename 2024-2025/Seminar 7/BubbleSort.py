def swap(a, b):
    if a > b:
        a, b = b, a
    return a, b

def bubble_sort(a):
    n = len(a)
    for i in range(1, n):
        for j in range(n - i):
            a[j], a[j + 1] = swap(a[j], a[j + 1])
            # if a[j] > a[j + 1]:
            #     a[j], a[j + 1] = a[j + 1], a[j]

sorted_array = [1,5,2,8,5,6,0]
bubble_sort(sorted_array)
print(sorted_array)