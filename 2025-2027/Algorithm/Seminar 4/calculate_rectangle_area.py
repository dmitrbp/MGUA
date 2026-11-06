# Линейный алгоритм вычисления площади прямоугольника
def calculate_rectangle_area():
    # Ввод данных
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    # Вычисление
    area = length * width

    # Вывод результата
    print(f"Площадь прямоугольника: {area}")


# Запуск алгоритма
calculate_rectangle_area()