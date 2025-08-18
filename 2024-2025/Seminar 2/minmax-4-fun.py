# Задаем значения чисел
a = int(input('Введите 1-ое число:'))
b = int(input('Введите 2-ое число:'))
c = int(input('Введите 3-ое число:'))
d = int(input('Введите 4-ое число:'))

# Используем встроенные функции для решения
min_value = min(a, b, c, d)
max_value = max(a, b, c, d)

# Выводим результаты
print("Min =", min_value)
print("Max =", max_value)
