def trip_planning():
    # Ввод данных
    distance = float(input("Расстояние до пункта назначения (км): "))
    fuel_consumption = float(input("Расход топлива (л/100км): "))
    fuel_price = float(input("Стоимость 1 литра топлива: "))

    # Вычисления
    fuel_needed = (distance / 100) * fuel_consumption
    trip_cost = fuel_needed * fuel_price

    # Вывод результатов
    print(f"\n--- Расчет поездки ---")
    print(f"Расстояние: {distance} км")
    print(f"Необходимо топлива: {fuel_needed:.1f} л")
    print(f"Стоимость поездки: {trip_cost:.2f} руб.")
    print(f"Стоимость туда и обратно: {trip_cost * 2:.2f} руб.")

trip_planning()