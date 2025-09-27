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

def check_leap_year(year):
    """
    Полная проверка с выводом результата
    """
    if is_leap_year(year):
        return f"{year} год - високосный"
    else:
        return f"{year} год - не високосный"

# Примеры использования
print(check_leap_year(2020))  # 2020 год - високосный
print(check_leap_year(2021))  # 2021 год - не високосный
print(check_leap_year(2000))  # 2000 год - високосный
print(check_leap_year(1900))  # 1900 год - не високосный