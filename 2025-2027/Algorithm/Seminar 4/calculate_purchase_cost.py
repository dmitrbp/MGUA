def calculate_purchase_cost():
    # Ввод данных
    price_per_item = float(input("Введите цену за единицу товара: "))
    quantity = int(input("Введите количество товара: "))
    discount_percent = float(input("Введите процент скидки: "))

    # Вычисления
    total_cost = price_per_item * quantity
    discount_amount = total_cost * (discount_percent / 100)
    final_cost = total_cost - discount_amount

    # Вывод результатов
    print(f"Общая стоимость: {total_cost:.2f}")
    print(f"Скидка: {discount_amount:.2f}")
    print(f"Итоговая стоимость: {final_cost:.2f}")


# Запуск алгоритма
calculate_purchase_cost()