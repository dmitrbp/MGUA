def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

unsorted = ["cat", "elephant", "fish", "dog", "butterfly"]
print(unsorted)
print(bubble_sort_by_length(unsorted))

