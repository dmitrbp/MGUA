price = int(input("Введите цену: "))
price_threshold  = int(input("Введите пороговую цену: "))
discount = int(input("Введите скидку: "))

if price > price_threshold:
    price = price * (1 - discount / 100)
    print(f"Применена скидка {discount}%!")

print(f"Итоговая цена: {price} руб.")