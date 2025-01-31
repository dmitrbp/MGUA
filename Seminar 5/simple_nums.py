def is_simple(n):
    for i in range(1, n + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
           print(i)

def is_simple2(n):
    for i in range(1, n + 1):
        is_simple = True
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                is_simple = False
                break
        if is_simple:
           print(i)

is_simple(20)

