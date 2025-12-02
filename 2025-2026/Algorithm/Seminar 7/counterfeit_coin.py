import random

def check_counterfeit_coin():
    """
    Находит фальшивую монету, которая имеет меньший вес,
    среди трех представленных
    Возможно только одно взвешивание
    """
    # Начальный массив весов из 3-х монет
    coins_def = [10, 10, 5]
    # Генерация случайного набора из начальных 3-х монет
    coins_set = random.sample(coins_def, 3)
    # Создание словаря из массива, чтобы добавить индексы (ключи)
    coins_dict = {i: coins_set[i] for i in range(0, len(coins_set))}
    print(f"coins_set = {coins_set}")
    print(f"coins_dict = {coins_dict}")
    # Выбираем случайным образом монету (ее индекс в словаре)
    index = random.randint(0, 2)
    # Вынимаем монету и удаляем ее из словаря
    index_value = {index:coins_dict.pop(index)}
    print(f"Случайно выбранная монета - {index_value}")
    # Оставшиеся в словаре ключи. В словаре осталось два элемента
    keys = list(coins_dict.keys())

    # Взвешиваем оставшиеся в словаре две монеты
    # Монеты равны по весу - вынутая монета фальшивая
    if coins_dict[keys[0]] == coins_dict[keys[1]]:
        print(f"Монета {index + 1} фальшивая")
    # Первая монета легче второй - первая фальшивая
    elif coins_dict[keys[0]] < coins_dict[keys[1]]:
        print(f"Монета {keys[0] + 1} фальшивая")
    # Вторая монета - фальшивая
    else:
        print(f"Монета {keys[1] + 1} фальшивая")

check_counterfeit_coin()