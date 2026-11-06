def unit_converter():
    """Конвертер различных единиц измерения"""
    value = float(input("Введите значение: "))

    # Метры в километры и сантиметры
    meters_to_km = value / 1000
    meters_to_cm = value * 100

    # Килограммы в граммы и тонны
    kg_to_grams = value * 1000
    kg_to_tons = value / 1000

    print(f"\n{value} метров = {meters_to_km} км = {meters_to_cm} см")
    print(f"{value} кг = {kg_to_grams} г = {kg_to_tons} т")


unit_converter()