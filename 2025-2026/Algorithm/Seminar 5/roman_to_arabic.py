def roman_to_arabic():
    """Преобразование римских чисел в арабские (упрощенная версия)"""
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman_number = input("Введите римское число: ").upper()
    arabic_number = sum([roman_numerals[key] for key in roman_number])
    print(f"{roman_number} = {arabic_number}")


roman_to_arabic()