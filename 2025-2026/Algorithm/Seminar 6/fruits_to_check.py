# Полное ветвление без elif: есть/нет в списке
fruits = ["apple", "banana", "orange"]
fruit_to_check = "apple"

if fruit_to_check in fruits:
    exists = "Найден в списке"
else:
    exists = "Не найден в списке"

print(f"Фрукт '{fruit_to_check}': {exists}")