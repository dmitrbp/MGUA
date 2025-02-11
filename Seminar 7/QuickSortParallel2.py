import datetime
import random
import time
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


def merge_parallels(l1, l2):
    r = []
    i, j = 0, 0
    while True:
        if i < len(l1):
            if j < len(l2):
                if l1[i] <= l2[j]:
                    r.append(l1[i])
                    i += 1
                else:
                    r.append(l2[j])
                    j += 1
            else:
                r.append(l1[i])
                i += 1
        else:
            if j < len(l2):
                r.append(l2[j])
                j += 1
            else:
                break
    return r


# Главная функция
def main():
    size_array = 1000000  # Размер массива
    array = [random.randint(1, 100000) for _ in range(size_array)]

    # Разделение массива на две части
    mid = len(array) // 2
    sub_array1 = array[:mid]
    sub_array2 = array[mid:]

    # Создание общего списка для записи результатов
    with Manager() as manager:
        result_list1 = manager.list()  # Общий список для результатов
        result_list2 = manager.list()

        # Запуск параллельных процессов
        process1 = Process(target=parallel_quick_sort, args=(sub_array1, result_list1))
        process2 = Process(target=parallel_quick_sort, args=(sub_array2, result_list2))

        time_start = time.time()  # Засекаем время начала работы
        process1.start()
        process2.start()
        process1.join()
        process2.join()

        # Слияние и окончательная сортировка
        final_sorted_array = merge_parallels(list(result_list1), list(result_list2))
        time_end = time.time()  # Засекаем время окончания работы
        # print("Итоговый отсортированный массив 1:", final_sorted_array)
        print("Время работы:", time_end - time_start)

    time_start = time.time()  # Засекаем время начала работы
    sorted_array = quick_sort(array)
    time_end = time.time()  # Засекаем время окончания работы
    # print("Итоговый отсортированный массив 2:", sorted_array)
    print("Время работы:", time_end - time_start)


if __name__ == "__main__":
    main()
