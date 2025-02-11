import random


def quick_sort(a):
    if len(a) > 1:
        q = random.choice(a)
        low = [n for n in a if n < q]
        eq = [q] * a.count(q)
        hi = [n for n in a if n > q]
        a = quick_sort(low) + eq + quick_sort(hi)

    return a

sorted_array = [1,5,2,8,9,6,3]
sorted_array = quick_sort(sorted_array)
print(sorted_array)