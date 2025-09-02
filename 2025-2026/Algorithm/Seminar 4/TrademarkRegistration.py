class TrademarkApplication:
    def __init__(self):
        self.trademark_name = ""
        self.mktu_classes = []
        self.application_type = "электронная"  # По умолчанию электронная подача

    def calculate_fees(self):
        """Расчет пошлин согласно тарифам Роспатента"""
        base_fee = 3500 if self.application_type == "электронная" else 4700
        class_fee = len(self.mktu_classes) * 1100
        examination_fee = 11500 if self.application_type == "электронная" else 13500

        total = base_fee + class_fee + examination_fee
        return total

    def generate_application(self):
        """Формирование заявки"""
        application_text = f"""
        ЗАЯВКА НА РЕГИСТРАЦИЮ ТОВАРНОГО ЗНАКА
        =====================================
        Наименование товарного знака: {self.trademark_name}
        Классы МКТУ: {', '.join(map(str, self.mktu_classes))}
        Тип подачи: {self.application_type}

        РАСЧЕТ ПОШЛИН:
        - Основная пошлина: {3500 if self.application_type == 'электронная' else 4700} руб.
        - Пошлина за классы МКТУ ({len(self.mktu_classes)}): {len(self.mktu_classes) * 1100} руб.
        - Пошлина за экспертизу: {11500 if self.application_type == 'электронная' else 13500} руб.
        - ИТОГО: {self.calculate_fees()} руб.
        """
        return application_text


def trademark_registration_assistant():
    """Ассистент по регистрации товарного знака"""
    print("🐅 АССИСТЕНТ РЕГИСТРАЦИИ ТОВАРНОГО ЗНАКА")
    print("=" * 50)

    app = TrademarkApplication()

    # Шаг 1: Название товарного знака
    app.trademark_name = input("Введите название товарного знака: ").strip()
    if not app.trademark_name:
        print("Ошибка: Название не может быть пустым!")
        return

    # Шаг 2: Выбор классов МКТУ
    print("\nВыберите классы МКТУ (введите числа через пробел):")
    print("Пример: 9 35 42 (для IT-компании)")
    print("Справочник: https://new.fips.ru/mktu/")

    try:
        classes_input = input("Классы МКТУ: ").strip()
        app.mktu_classes = list(map(int, classes_input.split()))
    except ValueError:
        print("Ошибка: Вводите только числа!")
        return

    if not app.mktu_classes:
        print("Ошибка: Необходимо выбрать хотя бы один класс МКТУ!")
        return

    # Шаг 3: Тип подачи
    print("\nВыберите тип подачи заявки:")
    print("1 - Электронная (дешевле)")
    print("2 - Бумажная")
    choice = input("Ваш выбор (1 или 2): ").strip()
    app.application_type = "электронная" if choice == "1" else "бумажная"

    # Расчет и вывод результатов
    total_fee = app.calculate_fees()
    application_text = app.generate_application()

    print("\n" + "=" * 50)
    print(application_text)
    print("=" * 50)

    # Инструкция по дальнейшим действиям
    print("\n📋 ИНСТРУКЦИЯ ПО ПОДАЧЕ:")
    print("1. Подайте заявку через портал ФИПС: https://new.fips.ru/")
    print("2. Оплатите пошлины через банк-клиент")
    print("3. Отслеживайте статус в личном кабинете")
    print("4. Срок рассмотрения: 12-18 месяцев")

    confirm = input("\nПодтверждаете формирование заявки? (да/нет): ").lower()
    if confirm == 'да':
        # Сохранение в файл (имитация)
        filename = f"заявка_на_ТЗ_{app.trademark_name[:10]}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(application_text)
        print(f"Заявка сохранена в файл: {filename}")
    else:
        print("Формирование заявки отменено.")


# Запуск ассистента
if __name__ == "__main__":
    trademark_registration_assistant()