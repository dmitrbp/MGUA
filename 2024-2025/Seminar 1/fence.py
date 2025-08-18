a = int(input('Введите А:'))
b = int(input('Введите Б:'))

# Периметр участка
d_fence = (a + b) * 2
# Суммарная длина досок
d_board = (d_fence / 0.2) * 2
# Количество досок
q_board = int(d_board / 4)

print('Кол-во досок: ', q_board)
