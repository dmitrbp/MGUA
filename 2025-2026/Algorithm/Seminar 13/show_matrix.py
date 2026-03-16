matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:          # Внешний цикл берет каждую строку
    for element in row:      # Внутренний цикл берет каждый элемент в строке
        print(element, end=" ")
    print()  # Новая строка
