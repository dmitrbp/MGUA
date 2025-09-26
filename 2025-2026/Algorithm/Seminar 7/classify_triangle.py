def classify_triangle(a, b, c):
    """
    Классифицирует треугольник по длинам сторон
    """
    # Проверка на существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"

    # Проверка типа треугольника
    if a == b == c:
        return "Равносторонний треугольник"
    elif a == b or a == c or b == c:
        return "Равнобедренный треугольник"
    else:
        # Проверка на прямоугольный треугольник
        sides = sorted([a, b, c])
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return "Прямоугольный треугольник"
        else:
            return "Разносторонний треугольник"


# Примеры использования
print(classify_triangle(3, 4, 5))  # Прямоугольный треугольник
print(classify_triangle(5, 5, 5))  # Равносторонний треугольник
print(classify_triangle(5, 5, 7))  # Равнобедренный треугольник
print(classify_triangle(2, 3, 4))  # Разносторонний треугольник
print(classify_triangle(2, 3, 10))  # Треугольник не существует