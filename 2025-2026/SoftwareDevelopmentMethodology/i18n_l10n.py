# Функция для определения единицы измерения температуры в зависимости от страны пользователя
def get_temperature_unit(country_code):
    if country_code in ['US', 'BS', 'BZ', 'KY', 'PW']:
        return 'Fahrenheit'
    else:
        return 'Celsius'

# Функция для конвертации температуры из Цельсия в Фаренгейт
def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

# Предположим, у нас есть температура в Цельсиях
current_temp_celsius = 20

# Определяем страну пользователя (пример)
user_country_code = 'US'  # Допустим, пользователь из США

# Получаем нужную единицу измерения для пользователя
temp_unit = get_temperature_unit(user_country_code)

# Если пользователь из США, конвертируем температуру в Фаренгейты
if temp_unit == 'Fahrenheit':
    current_temp = celsius_to_fahrenheit(current_temp_celsius)
    print(f"Current temperature: {current_temp}°F")
else:
    print(f"Current temperature: {current_temp_celsius}°C")