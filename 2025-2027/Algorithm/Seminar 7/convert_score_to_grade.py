def score_to_grade(score):
    """
    Конвертирует числовую оценку в буквенную
    """
    if score < 0 or score > 100:
        return "Некорректная оценка"

    step = 100 // 4

    if score > 100 - step:
        grade = "A"
        comment = "Отлично"
    elif score > 100 - 2 * step:
        grade = "B"
        comment = "Хорошо"
    elif score > 100 - 3 * step:
        grade = "C"
        comment = "Удовлетворительно"
    else:
        grade = "D"
        comment = "Неудовлетворительно"

    return f"Числовая оценка: {score} Буквенная оценка: {grade} ({comment})"


# Примеры использования
print(score_to_grade(95))  # Оценка: A (Отлично)
print(score_to_grade(71))  # Оценка: B (Хорошо)
print(score_to_grade(40))  # Оценка: C (Удовлетворительно)
print(score_to_grade(20))  # Оценка: D (Неудовлетворительно)