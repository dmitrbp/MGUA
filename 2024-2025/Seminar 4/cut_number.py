n = int(input('Введите исходное число N: '))
d = int(input('Введите исключаемую цифру I: '))

nr = 0
step = 0
while (n > 0):
    i = n % 10
    if i != d:
        nr = nr + i * 10 ** step
        step += 1
    n = n // 10
    
print('Усеченное число NI:', nr)
