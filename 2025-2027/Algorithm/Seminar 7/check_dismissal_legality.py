def check_dismissal_legality():
    print("\n=== АЛГОРИТМ ПРОВЕРКИ ЗАКОННОСТИ УВОЛНЕНИЯ ===\n")

    issues = []  # Список для сбора нарушений

    # Ветвление 1: Инициатор увольнения
    is_employer_initiated = input("Увольнение по инициативе работодателя? (да/нет): ").lower().strip() == 'да'

    if not is_employer_initiated:
        print("✓ Проверка оснований по заявлению работника (собственное желание, соглашение сторон)")
        return "Увольнение законно (инициатива работника)"

    # Ветвление 2: Выплата пособия
    severance_paid = input("Выплачено выходное пособие? (да/нет): ").lower().strip() == 'да'
    if not severance_paid:
        issues.append("Не выплачено выходное пособие")

    # Ветвление 3: Основание увольнения
    dismissal_reason = input("Основание увольнения (сокращение/прогул/другое): ").lower().strip()

    if dismissal_reason == 'сокращение':
        # Проверка условий для сокращения
        print("\n--- Проверка условий для увольнения по сокращению ---")

        vacancies_offered = input("Предложены все имеющиеся вакансии? (да/нет): ").lower().strip() == 'да'
        if not vacancies_offered:
            issues.append("Не предложены вакансии")

        two_months_notice = input("Уведомление направлено за 2 месяца? (да/нет): ").lower().strip() == 'да'
        if not two_months_notice:
            issues.append("Нарушен срок уведомления")

        union_consulted = input("Учтено мнение профсоюза (если он есть)? (да/нет): ").lower().strip() == 'да'
        if not union_consulted:
            issues.append("Не учтено мнение профсоюза")

    elif dismissal_reason == 'прогул':
        print("\n--- Проверка условий для увольнения за прогул ---")

        has_explanation = input("Работник предоставил объяснительную? (да/нет): ").lower().strip() == 'да'
        if not has_explanation:
            issues.append("Не запрошена объяснительная")

        absence_confirmed = input("Отсутствие подтверждено документально? (да/нет): ").lower().strip() == 'да'
        if not absence_confirmed:
            issues.append("Отсутствие не подтверждено")

    # Вывод результата
    if issues:
        print(f"\n✗ ВЫСОКИЙ РИСК ПРИЗНАНИЯ УВОЛЬНЕНИЯ НЕЗАКОННЫМ")
        print("Нарушения:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
        return "Увольнение с нарушениями"
    else:
        print("\n✓ УВОЛЬНЕНИЕ СООТВЕТСТВУЕТ ТРЕБОВАНИЯМ ЗАКОНОДАТЕЛЬСТВА")
        return "Увольнение законно"


# Запуск алгоритма
result = check_dismissal_legality()
print(f"\nИтоговый вердикт: {result}")