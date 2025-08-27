a = int(input('Введите 1-ое число:'))
b = int(input('Введите 2-ое число:'))
c = int(input('Введите 3-ое число:'))
d = int(input('Введите 4-ое число:'))

# начальное инициализация min и max первым числом a
min = a
max = a

# анализируем b
if b < min:
    min = b
# можно условие else оформить в две строчки
else:
    if b > max:
        max = b
# а можно в одну
# elif b > max:
#    max = b

# анализируем c
if c < min:
    min = c
elif c > max:
    max = c
    
# анализируем d
if d < min:
    min = d
elif d > max:
    max = d
    
print('Min = ', min, 'Max = ', max)