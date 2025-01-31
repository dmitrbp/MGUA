source = """Эта строка подготовлена для подсчета количества пробелов в ней
и для перевода следующих за пробелом букв в заглавные"""

result = ''
space_count = 0
next_flag = False
for ch in source:
    if ch == ' ' or ch == '\n':
        space_count += 1
        next_flag = True
    elif next_flag:
        next_flag = False;
        ch = ch.upper()
    result += ch
print(f'Количество пробелов: {space_count}')
print(result)