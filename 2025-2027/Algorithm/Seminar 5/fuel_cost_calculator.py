def fuel_cost_calculator():
    """Расчет стоимости топлива для поездки"""
    distance = float(input("Расстояние поездки (км): "))
    fuel_consumption = float(input("Расход топлива (л/100км): "))
    fuel_price = float(input("Цена топлива (руб/л): "))

    fuel_needed = (distance * fuel_consumption) / 100
    total_cost = fuel_needed * fuel_price

    print(f"Необходимо топлива: {fuel_needed:.2f} л")
    print(f"Общая стоимость: {total_cost:.2f} руб")


fuel_cost_calculator()