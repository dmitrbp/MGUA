# Обратный отсчет с проверкой начального условия
import time

countdown = int(input('countdown = '))
if countdown > 0:
    print("Начинаем обратный отсчет:")
    while countdown > 0:  # Проверка ПЕРЕД выполнением
        time.sleep(1)
        print(f"Осталось: {countdown}")
        countdown -= 1

    print("Запуск!")
else:
    print("Цикл не выполнился ни разу!")