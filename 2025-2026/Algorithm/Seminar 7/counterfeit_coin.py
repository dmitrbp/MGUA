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
    coins_dict = {i: coins_set[i] for i in range(0, len(coins_set))}
    print(f"coins_set = {coins_set}")
    print(f"coins_dict = {coins_dict}")
    index = random.randint(0, 2)
    index_value = {index:coins_dict.pop(index)}
    print(f"Случайно выбранная монета - {index_value}")
    keys = list(coins_dict.keys())

    if coins_dict[keys[0]] == coins_dict[keys[1]]:
        print(f"Монета {index + 1} фальшивая")
    elif coins_dict[keys[0]] < coins_dict[keys[1]]:
        print(f"Монета {keys[0] + 1} фальшивая")
    else:
        print(f"Монета {keys[1] + 1} фальшивая")

check_counterfeit_coin()