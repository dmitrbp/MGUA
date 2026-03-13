# Нахождение наибольшего общего делителя (НОД)
def gcd(a, b):
    """Алгоритм Евклида для нахождения НОД"""
    while b:
        c = a % b
        a = b
        b = c
        # a, b = b, a % b
    return abs(a)

for i in range(0, 10):
    j = i * (i - 1)
    k = i * (i + 1)
    print(f'Число 1: {j}, Число {k}: k, НОД: {gcd(j, k)}')