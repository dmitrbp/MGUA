n = int(input('Введите число:'))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f'Iteration {i}: -> factorial = {int(factorial / i)} * {i} = {factorial}')
print(f'{n}! = {factorial}')