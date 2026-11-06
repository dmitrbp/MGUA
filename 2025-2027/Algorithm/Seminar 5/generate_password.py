import random
import string


def generate_password():
    """Генерация случайного пароля заданной длины"""
    length = int(input("Введите длину пароля: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"Сгенерированный пароль: {password}")


generate_password()