def currency_converter():
    # Ввод данных
    amount = float(input("Введите сумму для конвертации: "))
    exchange_rate = float(input("Введите курс обмена: "))

    # Конвертация
    converted_amount = amount * exchange_rate

    # Вывод результата
    print(f"{amount} по курсу {exchange_rate} = {converted_amount:.2f}")


# Запуск алгоритма
currency_converter()