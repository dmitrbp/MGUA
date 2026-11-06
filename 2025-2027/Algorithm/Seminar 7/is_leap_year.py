def is_leap_year(year):
    """
    Проверяет, является ли год високосным
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# Пример использования
# -------------------------
# 2020 год - високосный
# 2021 год - не високосный
# 2000 год - високосный
# 1900 год - не високосный

year = int(input("Введите год для определения: "))
is_value = is_leap_year(year)
if(is_value):
    print(f"{year} год - високосный")
else:
    print(f"{year} год - не високосный")
