from sys import setrecursionlimit


def fibonacci(n):
    # Базовые случаи
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Рекурсивный случай
    f = fibonacci(n - 1) + fibonacci(n - 2)
    print(f)
    return f

# setrecursionlimit(10000)
f1 = fibonacci(20)
print(f1)