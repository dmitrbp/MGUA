def factorial_down(n):
    # 1. Базовый случай
    if n <= 1:
        return 1
    # 2. Рекурсивный случай
    else:
        return n * factorial_down(n - 1)


def factorial_up(n, current=1, acc=1):
    """
    n - целевое число
    current - текущее число, с которым работаем (начинаем с 1)
    acc - накопленное произведение (начинаем с 1)
    """
    # Базовый случай: дошли до цели
    if current > n:
        return acc

    # Рекурсивный случай: умножаем аккумулятор на current и идем к current+1
    return factorial_up(n, current + 1, acc * current)



print(factorial_down(5))  # Вывод: 120
print(factorial_up(5))
