a1 = 1  # первый элемент
d = int(input('разность: '))
n = int(input('кол-во элементов: '))
sum_ap = 0

for i in range(n):
    current = a1 + i * d  # вычисляем текущий элемент
    sum_ap += current     # добавляем к сумме

print(f'сумма = {sum_ap}')