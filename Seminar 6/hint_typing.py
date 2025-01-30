# Динамическая типизация с подсказками
v1 : int = 10
v2 : float = 3.14
v3 : str = 'Это строка'
v4 : bool = True
print(f'v1 is {type(v1)}')
print(f'v2 is {type(v2)}')
print(f'v3 is {type(v3)}')
print(f'v4 is {type(v4)}')

print('----------------------')

v4 = 10
v3 = 3.14
v2 = 'Это строка'
v1 = True
print(f'v1 is {type(v1)}')
print(f'v2 is {type(v2)}')
print(f'v3 is {type(v3)}')
print(f'v4 is {type(v4)}')

