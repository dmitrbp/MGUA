def bubble_sort(a):
    n = len(a)
    for i in range(1, n):
        for j in range(n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

sorted_array = [4,3,6,1,5,2]
bubble_sort(sorted_array)
print(sorted_array)