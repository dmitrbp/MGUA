def calculate_average():
    # Ввод трех чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    # Вычисление среднего
    average = (num1 + num2 + num3) / 3

    # Вывод результата
    print(f"Среднее арифметическое: {average:.2f}")


# Запуск алгоритма
calculate_average()