def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)

print(summa(4))
