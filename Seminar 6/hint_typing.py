s: str = "Hello, world!"
# Ошибка - переменная s должна быть строчным значением
s = 10
print(s)  # Вывод: 10

def multiply(x: int, y: int) -> int:
    return x * y

result1 = multiply(5, 10)
print(result1)  # Вывод: 50

# Ошибка типа - второй аргумент должен быть целым числом
result2 = multiply(5, "hello")
print(result2) # Вывод: hellohellohellohellohello

# Ошибка - переменная result3 должна быть строчным значением
result3:str = multiply(10, 20)
print(result3)  # Вывод: 200
