def compound_interest():
    """Расчет конечной суммы при сложном проценте"""
    principal = float(input("Начальная сумма: "))
    rate = float(input("Годовая процентная ставка (%): "))
    years = int(input("Количество лет: "))

    amount = principal * (1 + rate / 100) ** years
    interest = amount - principal

    print(f"Конечная сумма: {amount:.2f}")
    print(f"Начисленные проценты: {interest:.2f}")


compound_interest()