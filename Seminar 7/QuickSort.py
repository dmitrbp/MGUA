import random


def quick_sort(a):
    if len(a) > 1:
        # pivot = random.choice(a)
        # pivot = a[len(a) // 2]
        pivot = a[len(a) - 1]
        low = [n for n in a if n < pivot]
        eq = [pivot] * a.count(pivot)
        hi = [n for n in a if n > pivot]
        print(f'low = {low}, eq = {eq}, hi = {hi}')
        a = quick_sort(low) + eq + quick_sort(hi)

    return a


sorted_array = [9, -3, 5, 2, 6, 8, -6, 1, 3]
print(sorted_array)
sorted_array = quick_sort(sorted_array)
print(sorted_array)
