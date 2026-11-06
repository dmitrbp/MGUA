# Конвертер градусов Цельсия в Фаренгейты
def celsius_to_fahrenheit():
    # Ввод температуры в Цельсиях
    celsius = float(input("Введите температуру в градусах Цельсия: "))

    # Формула конвертации
    fahrenheit = (celsius * 9 / 5) + 32

    # Вывод результата
    print(f"{celsius}°C = {fahrenheit}°F")


# Запуск алгоритма
celsius_to_fahrenheit()