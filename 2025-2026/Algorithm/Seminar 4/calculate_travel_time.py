def calculate_travel_time():
    # Ввод данных
    distance = float(input("Введите расстояние (км): "))
    speed = float(input("Введите среднюю скорость (км/ч): "))

    # Вычисление времени
    time_hours = distance / speed
    time_minutes = time_hours * 60

    # Вывод результата
    print(f"Время в пути: {time_hours:.2f} часов")
    print(f"Или {time_minutes:.2f} минут")


# Запуск алгоритма
calculate_travel_time()