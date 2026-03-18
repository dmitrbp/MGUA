import time
from sys import setrecursionlimit

def fibonacci(n):
    # Базовые случаи
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Рекурсивный случай
    f = fibonacci(n - 1) + fibonacci(n - 2)
    return f

def fibonacci_memo(n, memo={}):
    # Проверяем, считали ли мы уже это число
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    # Сохраняем результат перед возвратом
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# setrecursionlimit(10000)
start_time = time.time()
f1 = fibonacci(40)
end_time = time.time()
print(f"f1 = {f1}, Elapsed: {(end_time - start_time):.8f} seconds")

start_time = time.time()
f2 = fibonacci_memo(40)
end_time = time.time()
print(f"f2 = {f2}, Elapsed: {(end_time - start_time):.8f} seconds")
