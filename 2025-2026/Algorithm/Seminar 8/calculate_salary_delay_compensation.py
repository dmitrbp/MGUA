def calculate_salary_delay_compensation():
    print("=== РАСЧЕТ КОМПЕНСАЦИИ ЗА ЗАДЕРЖКУ ЗАРПЛАТЫ ===\n")

    salary_amount = float(input("Сумма задолженности по зарплате (руб.): "))
    delay_days = int(input("Количество дней задержки: "))

    # Ставка рефинансирования ЦБ (пример)
    refinancing_rate = 7.5

    # Расчет компенсации
    daily_rate = refinancing_rate / 100 / 300
    compensation = salary_amount * daily_rate * delay_days

    # Ветвление по размеру компенсации
    if delay_days == 0:
        print("Задержки нет - компенсация не начисляется")

    elif delay_days < 15:
        print(f"✓ Компенсация за {delay_days} дней: {compensation:.2f} руб.")
        print("Незначительная задержка")

    elif 15 <= delay_days <= 30:
        print(f"✓ Компенсация за {delay_days} дней: {compensation:.2f} руб.")
        print("Существенная задержка - можно жаловаться в трудовую инспекцию")

    else:
        # Увеличенная компенсация за длительную задержку
        enhanced_compensation = compensation * 1.5
        print(f"✓ Увеличенная компенсация за {delay_days} дней: {enhanced_compensation:.2f} руб.")
        print("⚠ Длительная задержка - срочно обращайтесь в инспекцию или суд!")


# Запуск
calculate_salary_delay_compensation()