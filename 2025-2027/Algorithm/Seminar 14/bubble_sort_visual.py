import time
import os


def bubble_sort_visual(arr, delay=0.5):
    """
    Сортировка пузырьком с визуализацией
    """
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("\n" + "=" * 50)
    print("НАЧАЛО СОРТИРОВКИ")
    print("=" * 50)
    display_array(arr, "Исходный массив")
    time.sleep(delay)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1
            print(f"\n--- Проход {i + 1}, сравнение {comparisons} ---")
            print(f"Сравниваем элементы: {arr[j]} (индекс {j}) и {arr[j + 1]} (индекс {j + 1})")

            display_array(arr, "Текущее состояние")
            highlight_elements(arr, j, j + 1)

            if arr[j] > arr[j + 1]:
                print(f"  → {arr[j]} > {arr[j + 1]}, меняем местами")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
                display_array(arr, f"После обмена (обменов: {swaps})")
            else:
                print(f"  → {arr[j]} <= {arr[j + 1]}, оставляем как есть")

            time.sleep(delay)

        print(f"\n✓ Проход {i + 1} завершен. Самый большой элемент '{arr[n - i - 1]}' всплыл в конец")
        display_array(arr, f"После прохода {i + 1}")

        if not swapped:
            print("\n✨ Массив уже отсортирован! Досрочное завершение.")
            break

        time.sleep(delay)

    print("\n" + "=" * 50)
    print(f"СОРТИРОВКА ЗАВЕРШЕНА!")
    print(f"Всего сравнений: {comparisons}")
    print(f"Всего обменов: {swaps}")
    print("=" * 50)
    display_array(arr, "Отсортированный массив")

    return arr


def display_array(arr, message):
    """Отображает массив в виде строки"""
    print(f"\n{message}:")
    print("┌" + "───" * len(arr) + "┐")
    print("│ " + " │ ".join(f"{x:3}" for x in arr) + " │")
    print("└" + "───" * len(arr) + "┘")
    print("  " + "   ".join(f"{i:3}" for i in range(len(arr))))


def highlight_elements(arr, idx1, idx2):
    """Подсвечивает сравниваемые элементы"""
    print("\nСравниваемые элементы:")
    print("┌" + "───" * len(arr) + "┐")
    items = []
    for i, x in enumerate(arr):
        if i == idx1 or i == idx2:
            items.append(f"[{x:3}]")
        else:
            items.append(f" {x:3} ")
    print("│ " + " │ ".join(items) + " │")
    print("└" + "───" * len(arr) + "┘")


def get_user_array():
    """Получает массив от пользователя"""
    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНАЯ СОРТИРОВКА ПУЗЫРЬКОМ")
    print("=" * 50)

    while True:
        try:
            choice = input(
                "\nВыберите вариант:\n1. Ввести свой массив\n2. Использовать пример\n3. Случайный массив\nВаш выбор (1-3): ")

            if choice == '1':
                arr_input = input("Введите числа через пробел: ")
                arr = [int(x) for x in arr_input.split()]
                if not arr:
                    print("Массив не может быть пустым!")
                    continue
                return arr

            elif choice == '2':
                print("\nПримеры массивов:")
                print("1. [64, 34, 25, 12, 22, 11, 90] - обычный")
                print("2. [5, 1, 4, 2, 8] - короткий")
                print("3. [1, 2, 3, 4, 5] - уже отсортированный")
                print("4. [5, 4, 3, 2, 1] - обратный порядок")

                ex_choice = input("Выберите пример (1-4): ")
                examples = {
                    '1': [64, 34, 25, 12, 22, 11, 90],
                    '2': [5, 1, 4, 2, 8],
                    '3': [1, 2, 3, 4, 5],
                    '4': [5, 4, 3, 2, 1]
                }

                if ex_choice in examples:
                    return examples[ex_choice]
                else:
                    print("Неверный выбор! Использую пример 1")
                    return [64, 34, 25, 12, 22, 11, 90]

            elif choice == '3':
                import random
                size = int(input("Введите размер массива (5-15): "))
                size = max(5, min(15, size))
                arr = [random.randint(1, 100) for _ in range(size)]
                print(f"Сгенерирован массив: {arr}")
                return arr
            else:
                print("Пожалуйста, выберите 1, 2 или 3")

        except ValueError:
            print("Ошибка! Пожалуйста, введите корректные числа.")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            exit()


def main():
    """Главная функция"""
    try:
        # Получаем массив от пользователя
        arr = get_user_array()

        print(f"\nИсходный массив: {arr}")

        # Настройка скорости
        print("\nНастройка скорости визуализации:")
        print("1. Медленно (1 секунда между шагами)")
        print("2. Средне (0.5 секунды)")
        print("3. Быстро (0.2 секунды)")
        print("4. Очень быстро (0.1 секунды)")

        speed_choice = input("Ваш выбор (1-4): ")
        speed_map = {'1': 1.0, '2': 0.5, '3': 0.2, '4': 0.1}
        delay = speed_map.get(speed_choice, 0.5)

        # Запускаем сортировку
        sorted_arr = bubble_sort_visual(arr.copy(), delay)

        # Проверка результата
        if sorted_arr == sorted(arr):
            print("\n✅ Сортировка выполнена успешно!")

        # Дополнительная информация
        print("\n📊 ИНФОРМАЦИЯ О СОРТИРОВКЕ:")
        print(f"• Сложность алгоритма: O(n²) в худшем случае")
        print(f"• Сложность в лучшем случае: O(n) (уже отсортирован)")
        print(f"• Память: O(1) - сортировка на месте")

    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"\n❌ Произошла ошибка: {e}")


if __name__ == "__main__":
    # Очистка консоли (опционально)
    # os.system('cls' if os.name == 'nt' else 'clear')
    main()