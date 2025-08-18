# Динамическая типизация
def print_results(v1, v2, v3, v4):
    print(f'v1 type is {type(v1)}, value = {v1}')
    print(f'v2 type is {type(v2)}, value = {v2}')
    print(f'v3 type is {type(v3)}, value = {v3}')
    print(f'v4 type is {type(v4)}, value = {v4}')
    print('-------------------------------------')

v1 = 10
v2 = 3.14
v3 = 'Это строка'
v4 = True
print_results(v1, v2, v3, v4)

v4 = 10
v3 = 3.14
v2 = 'Это строка'
v1 = True
print_results(v1, v2, v3, v4)
