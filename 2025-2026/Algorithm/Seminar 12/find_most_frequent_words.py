# Вспомогательный алгоритм 1: Очистка слова от знаков препинания
def clean_word(raw_word):
    return ''.join(char.lower() for char in raw_word if char.isalpha())


# Вспомогательный алгоритм 2: Подсчет частот
def count_frequencies(words_list):
    freq = {}
    for word in words_list:
        freq[word] = freq.get(word, 0) + 1
    return freq


# Вспомогательный алгоритм 3: Поиск максимума в словаре
def get_max_frequency(freq_dict):
    if not freq_dict:
        return 0
    return max(freq_dict.values())


# Основной алгоритм
def find_most_frequent_words(text):
    # Шаг 1: Разбиваем и чистим
    raw_words = text.split()
    cleaned = [clean_word(w) for w in raw_words if clean_word(w)]

    # Шаг 2: Считаем частоты
    frequencies = count_frequencies(cleaned)

    # Шаг 3: Находим максимум
    max_freq = get_max_frequency(frequencies)

    # Шаг 4: Отбираем результат
    result = [word for word, count in frequencies.items() if count == max_freq]

    return result

print(find_most_frequent_words(
    "This is the first sentence. This is for clean and for frequency calculation. It is sample")
)