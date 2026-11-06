# Реализация функции
def find_max(arr):
    if not arr:  # Обработка краевого случая - пустой массив
        return None
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

# Набор тестов (тестовый сценарий)
def test_find_max():
    # Стандартный случай
    assert find_max([1, 2, 3, 4]) == 4, "Ошибка в стандартном случае"
    # Краевые случаи
    assert find_max([]) is None, "Ошибка при работе с пустым массивом"
    assert find_max([7]) == 7, "Ошибка при работе с одним элементом"
    assert find_max([-1, -5, -3]) == -1, "Ошибка при работе с отрицательными числами"
    assert find_max([5, 3, 5, 2]) == 5, "Ошибка при повторяющемся максимуме"
    print("Все тесты прошли успешно!")

# Запуск тестов
test_find_max()