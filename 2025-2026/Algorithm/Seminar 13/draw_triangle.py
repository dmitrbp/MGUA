rows = 5
cols = 5

step = round(cols / rows)

for i in range(rows):        # Для каждой строки
    for j in range(cols):     # Рисуем звездочеки в ряд
        print("*", end="")
    cols -= step
    print()  # Переходим на новую строку

#----------------------------------------------------------

size = 5

for i in range(size):
    for j in range(size - i):
        print("*", end="")
    print()