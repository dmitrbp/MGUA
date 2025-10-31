def calc_calories():
    # Ввод данных
    proteins = float(input("Белки (г): "))
    fats = float(input("Жиры (г): "))
    carbs = float(input("Углеводы (г): "))

    # Вычисления
    calories = proteins * 4 + fats * 9 + carbs * 4

    # Вывод результатов
    print(f"\nПищевая ценность:")
    print(f"Белки: {proteins} г")
    print(f"Жиры: {fats} г")
    print(f"Углеводы: {carbs} г")
    print(f"Калорийность: {calories} ккал")

calc_calories()