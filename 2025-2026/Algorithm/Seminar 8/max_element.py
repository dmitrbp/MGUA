def calc_max_element(arr):
    # предполагаем, что первый элемент - максимальный
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            # обновляем максимум
            max_element = arr[i]
    return max_element

arr = [3, 7, 2, 9, 1, 8]
max_element = calc_max_element(arr)
print(f'Array is {arr}')
print(f'Maximum = {max_element}')
