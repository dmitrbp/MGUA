a, b, c, d = input("Введите 4 числа через запятую:\n").split(',')

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
