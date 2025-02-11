import random
from multiprocessing import Process, Manager


# Функция быстрой сортировки
def quick_sort(a):
    if len(a) > 1:
        q = random.choice(a)
        low = [n for n in a if n < q]
        eq = [q] * a.count(q)
        hi = [n for n in a if n > q]
        a = quick_sort(low) + eq + quick_sort(hi)
    return a


# Функция для параллельной быстрой сортировки
def parallel_quick_sort(array, result_list):
    sorted_array = quick_sort(array)
    result_list.extend(sorted_array)  # Записываем результат в общий список


# Главная функция
def main():
    size_array = 2 ** 5  # Размер массива
    array = [random.randint(1, 100) for _ in range(size_array)]

    # Разделение массива на две части
    mid = len(array) // 2
    sub_array1 = array[:mid]
    sub_array2 = array[mid:]

    # Создание общего списка для записи результатов
    with Manager() as manager:
        result_list = manager.list()  # Общий список для результатов

        # Запуск параллельных процессов
        process1 = Process(target=parallel_quick_sort, args=(sub_array1, result_list))
        process2 = Process(target=parallel_quick_sort, args=(sub_array2, result_list))

        process1.start()
        process2.start()

        process1.join()
        process2.join()

        # Слияние и окончательная сортировка
        intermidiant_sorted_array = list(result_list)
        final_sorted_array = quick_sort(list(result_list))
        print("Итоговый отсортированный массив:", final_sorted_array)


if __name__ == "__main__":
    main()
