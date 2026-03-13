# Проверка анаграммы
def are_anagrams(str1, str2):
    """Проверяет, составлены ли строки из одних и тех же букв"""
    return sorted(str1.lower()) == sorted(str2.lower())

pair_words_list = \
    [['Кабан', 'банка'], ['Колчан', 'качан'], ['Мышка', 'камыш'],
     ['Взгляд', 'вздох'], ['Коршун', 'шнурок']]

for pair_words in pair_words_list:
    print(f'pair_words - {pair_words}, ' 
          f'is_anagram - {are_anagrams(pair_words[0], pair_words[1])}')