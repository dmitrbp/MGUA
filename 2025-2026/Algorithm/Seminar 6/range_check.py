# Полное ветвление без elif: в диапазоне/вне диапазона
x = 25
min_val = 10
max_val = 100

if min_val <= x <= max_val:
    in_range = "В диапазоне"
else:
    in_range = "Вне диапазона"

print(f"Число {x}: {in_range}")