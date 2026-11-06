def multiplication_table():
    """Генерация таблицы умножения для заданного числа"""
    number = int(input("Введите число для таблицы умножения: "))

    print(f"\nТаблица умножения для {number}:")

    res = [f"\n{number} * {i} = {number * i}" for i in range(1,11)]

    print(*res)


multiplication_table()