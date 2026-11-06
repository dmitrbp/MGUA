def calculator(a, b, operation):
    """
    Выполняет арифметические операции над двумя числами
    """
    if operation == '+':
        result = a + b
        print(f"{a} + {b} = {result}")
    elif operation == '-':
        result = a - b
        print(f"{a} - {b} = {result}")
    elif operation == '*':
        result = a * b
        print(f"{a} * {b} = {result}")
    elif operation == '/':
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Ошибка: деление на ноль!")
            return None
    else:
        print("Неизвестная операция")
        return None

    return result


# Примеры использования
calculator(10, 5, '+')  # 10 + 5 = 15
calculator(10, 5, '-')  # 10 - 5 = 5
calculator(10, 5, '*')  # 10 * 5 = 50
calculator(10, 5, '/')  # 10 / 5 = 2.0
calculator(10, 0, '/')  # Ошибка: деление на ноль!