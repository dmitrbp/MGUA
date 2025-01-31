n = int(input('Введите исходное число N:'))
ni = 0
while (n > 0):
    i = n % 10
    n = n // 10
    ni = (ni * 10 + i)
    print(f'i={i}, n={n}, ni={ni}')
print('Инвертированное число NI:', ni)
