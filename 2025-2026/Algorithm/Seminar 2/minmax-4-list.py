# Задаем значения чисел
a = int(input('Введите 1-ое число:'))
b = int(input('Введите 2-ое число:'))
c = int(input('Введите 3-ое число:'))
d = int(input('Введите 4-ое число:'))

# Создаем массив (список) из введенных чисел
numbers = [a, b, c, d]

# Находим минимальное и максимальное значения
min_value = numbers[0]
max_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number

# Выводим результаты
print("Min =", min_value)
print("Max =", max_value)

