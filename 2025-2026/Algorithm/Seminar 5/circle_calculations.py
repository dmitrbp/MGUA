def circle_calculations():
    """Вычисление периметра и площади круга по радиусу"""
    radius = float(input("Введите радиус круга: "))

    pi = 3.14159
    perimeter = 2 * pi * radius
    area = pi * radius ** 2

    print(f"Периметр круга: {perimeter:.2f}")
    print(f"Площадь круга: {area:.2f}")


circle_calculations()