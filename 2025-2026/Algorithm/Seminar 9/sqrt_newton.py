# Вычисление квадратного корня методом Ньютона
def sqrt_newton(n, epsilon=1e-10):
    if n < 0:
        return None

    guess = n / 2.0  # Начальное приближение
    prev_guess = 0

    # Продолжаем, пока разница между итерациями существенна
    while abs(guess - prev_guess) > epsilon:
        prev_guess = guess
        guess = (guess + n / guess) / 2  # Формула Ньютона

        print(f"Приближение: {guess}")

    return guess


n = 25
print(f"Исходное число: {n}")
result = sqrt_newton(n)
print(f"Квадратный корень: {result}")