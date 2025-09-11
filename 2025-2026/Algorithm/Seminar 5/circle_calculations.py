def circle_calculations():
    """Вычисление периметра и площади круга по радиусу"""
    radius = float(input("Введите радиус круга: "))

    perimeter = 2 * 3.14159 * radius
    area = 3.14159 * radius ** 2

    print(f"Периметр круга: {perimeter:.2f}")
    print(f"Площадь круга: {area:.2f}")


circle_calculations()