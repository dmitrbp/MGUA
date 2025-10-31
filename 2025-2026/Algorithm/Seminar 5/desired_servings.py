def desired_servings():
    # Исходные данные (ингредиенты для 4 порций)
    flour_original = 200  # грамм
    sugar_original = 100  # грамм
    eggs_original = 2     # штуки

    # Ввод данных
    original_servings = 4
    desired_servings = int(input("На сколько порций пересчитать рецепт? "))

    # Вычисления
    coefficient = desired_servings / original_servings
    flour_new = flour_original * coefficient
    sugar_new = sugar_original * coefficient
    eggs_new = eggs_original * coefficient

    # Вывод результатов
    print(f"\nРецепт на {desired_servings} порций:")
    print(f"Мука: {flour_new:.0f} г")
    print(f"Сахар: {sugar_new:.0f} г")
    print(f"Яйца: {eggs_new:.0f} шт")

desired_servings()