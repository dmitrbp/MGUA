def roman_to_arabic():
    """Преобразование римских чисел в арабские (упрощенная версия)"""
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman_number = input("Введите римское число: ").upper()

    # arabic_number = sum([roman_numerals[key] for key in roman_number])
    # print(f"{roman_number} = {arabic_number}")

    index = 0
    arabic_number = 0
    while index < len(roman_number):
        if index == len(roman_number) - 1 or roman_numerals[roman_number[index]] >= roman_numerals[roman_number[index + 1]]:
            arabic_number += roman_numerals[roman_number[index]]
            index += 1
        else:
            arabic_number += roman_numerals[roman_number[index +1]] - roman_numerals[roman_number[index]]
            index += 2
    print(f"{roman_number} = {arabic_number}")

roman_to_arabic()