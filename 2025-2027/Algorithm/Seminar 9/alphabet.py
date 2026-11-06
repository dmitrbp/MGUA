russian_alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
russian_vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
sentense = 'Как упоительны в России вечера, как свежи и дивны ночи'

result1 = ''.join([ch for ch in sentense if ch in russian_vowels])
result2 = ''.join([ch for ch in sentense if not ch in russian_vowels and ch in russian_alphabet])

print (result1)
print (result2)
