def calculate_court_fee(claim_amount):
    if claim_amount <= 100000:
        return claim_amount * 0.04  # 4% от суммы иска
    elif 100000 < claim_amount <= 200000:
        return 4000 + (claim_amount - 100000) * 0.03
    elif 200000 < claim_amount <= 1000000:
        return 7000 + (claim_amount - 200000) * 0.02
    else:
        return 25000 + (claim_amount - 1000000) * 0.01


# Пример использования
print(calculate_court_fee(500000))  # Вывод: 13000
