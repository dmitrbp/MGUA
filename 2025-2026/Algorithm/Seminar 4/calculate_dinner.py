def calculate_dinner():
    t = [a, b, c, d] = (
        list(map(int, input('Введите значения через запятую: ').split(',')))
    )
    s1 = sum(t)
    s2 = s1 + b
    rel = s2 / s1
    print(f'Начальная стоимость: {s1} \nУвеличение, раз: {rel}')

calculate_dinner()