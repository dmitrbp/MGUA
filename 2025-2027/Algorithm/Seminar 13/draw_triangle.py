rows = 5
cols = 5

step = round(cols / rows)

for _ in range(rows):        # Для каждой строки
    for _ in range(cols):     # Рисуем звездочеки в ряд
        print("*", end="")
    cols -= step
    print()  # Переходим на новую строку

print('----------------------------------------------------------')

size = 5

for i in range(size):
    for _ in range(size - i):
        print("*", end="")
    print()