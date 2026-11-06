# Компактный пример с меню выбора
while True:
    choice = input("Выберите: 1-Привет, 2-Пока, 0-Выход: ")

    if choice == '1':
        print("Привет!")
    elif choice == '2':
        print("Пока!")
    elif choice == '0':
        print("Выход...")
        break
    else:
        print("Неверный выбор!")