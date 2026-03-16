rows = 5
cols = 5

cols_limit = cols
step = round(cols / rows)

for i in range(rows):        # Для каждой строки
    for j in range(cols_limit):     # Рисуем звездочеки в ряд
        print("*", end="")
    cols_limit -= step
    print()  # Переходим на новую строку