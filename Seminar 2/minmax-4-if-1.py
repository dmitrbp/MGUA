a = int(input('Введите 1-ое число:'))
b = int(input('Введите 2-ое число:'))
c = int(input('Введите 3-ое число:'))
d = int(input('Введите 4-ое число:'))

# проверяем на минимакс A
if a < b and a < c and a < d:
    print('Min=', a)
if a > b and a > c and a > d:
    print('Max=', a)
    
# проверяем на минимакс B
if b < a and b < c and b < d:
    print('Min=', b)
if b > a and b > c and b > d:
    print('Max=', b)

# проверяем на минимакс C
if c < a and c < d and c < d:
    print('Min=', c)
if c > a and c > d and c > d:
    print('Max=', c)

# проверяем на минимакс D
if d < a and d < b and d < c:
    print('Min=', d)
if d > a and d > b and d > c:
    print('Max=', d)

