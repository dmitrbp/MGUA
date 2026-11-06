def qualify_theft():
    print("\n=== АЛГОРИТМ КВАЛИФИКАЦИИ ХИЩЕНИЯ ===\n")

    # Ветвление 1: Тайность изъятия
    is_secret = input("Изъятие имущества было тайным? (да/нет): ").lower().strip() == 'да'

    if not is_secret:
        # Ветвление 2: Применение насилия для грабежа
        has_violence = input("Применялось ли насиление? (да/нет): ").lower().strip() == 'да'

        if has_violence:
            # Ветвление 3: Опасность насилия
            is_dangerous_violence = input("Насилие было опасным для жизни/здоровья? (да/нет): ").lower().strip() == 'да'

            if is_dangerous_violence:
                qualification = "РАЗБОЙ (ст. 162 УК РФ)"
                punishment = "Лишение свободы до 8-15 лет"
            else:
                qualification = "ГРАБЕЖ с применением насилия (ч. 2 ст. 161 УК РФ)"
                punishment = "Лишение свободы до 7 лет"
        else:
            qualification = "ГРАБЕЖ (ст. 161 УК РФ)"
            punishment = "Лишение свободы до 4 лет"
    else:
        # Ветвление для кражи
        theft_value = input("Стоимость похищенного (крупный/значительный/незначительный): ").lower().strip()

        if theft_value == 'крупный':
            qualification = "КРАЖА в крупном размере (ч. 3 ст. 158 УК РФ)"
            punishment = "Лишение свободы до 6 лет"
        elif theft_value == 'значительный':
            qualification = "КРАЖА (ч. 1 ст. 158 УК РФ)"
            punishment = "Лишение свободы до 2 лет"
        else:
            qualification = "МЕЛКОЕ ХИЩЕНИЕ (КоАП РФ)"
            punishment = "Административный арест или штраф"

    # Вывод результата
    print(f"\n=== РЕЗУЛЬТАТ КВАЛИФИКАЦИИ ===")
    print(f"Квалификация: {qualification}")
    print(f"Возможное наказание: {punishment}")

    return qualification


# Запуск алгоритма
result = qualify_theft()
print(f"\nОкончательная квалификация: {result}")