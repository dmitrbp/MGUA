import re
from datetime import datetime


class RealEstateChecker:
    def __init__(self):
        self.cadastral_number = ""
        self.ownership_data = None
        self.encumbrances = []
        self.vri_data = None

    def validate_cadastral_number(self, number):
        """Проверка формата кадастрового номера"""
        pattern = r'^\d{2}:\d{2}:\d{6,7}:\d+$'
        return re.match(pattern, number) is not None

    def mock_api_call(self, endpoint, params):
        """Имитация запроса к API Росреестра"""
        # В реальности здесь был бы requests.get()
        mock_data = {
            'ownership': {
                'status': 'зарегистрировано',
                'owner': 'Иванов Иван Иванович',
                'registration_date': '2020-05-15',
                'share': '1/1'
            },
            'encumbrances': [
                {
                    'type': 'ипотека',
                    'registrator': 'АО "Сбербанк"',
                    'date': '2020-05-15',
                    'number': '123-456'
                }
            ],
            'vri': {
                'code': '141001000000',
                'description': 'Для размещения объектов торговли',
                'permitted_use': 'Магазин розничной торговли'
            }
        }
        return mock_data.get(endpoint, {})

    def check_ownership(self):
        """Проверка права собственности"""
        if not self.validate_cadastral_number(self.cadastral_number):
            return {"error": "Неверный формат кадастрового номера"}

        self.ownership_data = self.mock_api_call('ownership',
                                                 {'cadastral_number': self.cadastral_number})
        return self.ownership_data

    def check_encumbrances(self):
        """Проверка обременений"""
        self.encumbrances = self.mock_api_call('encumbrances',
                                               {'cadastral_number': self.cadastral_number})
        return self.encumbrances

    def check_vri(self):
        """Проверка вида разрешенного использования"""
        self.vri_data = self.mock_api_call('vri',
                                           {'cadastral_number': self.cadastral_number})
        return self.vri_data

    def generate_report(self):
        """Формирование отчета о правовом режиме"""
        report = f"""
        ОТЧЕТ О ПРАВОВОМ РЕЖИМЕ ОБЪЕКТА НЕДВИЖИМОСТИ
        ============================================
        Кадастровый номер: {self.cadastral_number}
        Дата проверки: {datetime.now().strftime('%d.%m.%Y %H:%M')}

        1. ПРАВО СОБСТВЕННОСТИ:
        {'Не найдено' if not self.ownership_data else f"""
           Статус: {self.ownership_data.get('status', 'нет данных')}
           Собственник: {self.ownership_data.get('owner', 'нет данных')}
           Дата регистрации: {self.ownership_data.get('registration_date', 'нет данных')}
           Доля: {self.ownership_data.get('share', 'нет данных')}
        """}

        2. ОБРЕМЕНЕНИЯ:
        {('Отсутствуют' if not self.encumbrances else
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               '\n'.join([f'   - {enc.get("type")} ({enc.get("registrator")})'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          for enc in self.encumbrances]))}

        3. ВИД РАЗРЕШЕННОГО ИСПОЛЬЗОВАНИЯ (ВРИ):
        {'Не найден' if not self.vri_data else f"""
           Код: {self.vri_data.get('code', 'нет данных')}
           Описание: {self.vri_data.get('description', 'нет данных')}
           Разрешенное использование: {self.vri_data.get('permitted_use', 'нет данных')}
        """}

        РЕКОМЕНДАЦИИ:
        {self.generate_recommendations()}
        """
        return report

    def generate_recommendations(self):
        """Генерация рекомендаций на основе данных"""
        recommendations = []

        if not self.ownership_data:
            recommendations.append("⚠️  Провести уточнение права собственности")

        if self.encumbrances:
            recommendations.append("⚠️  Учесть наличие обременений при сделке")

        if self.vri_data and 'жилой' in self.vri_data.get('description', '').lower():
            recommendations.append("✅ ВРИ соответствует жилому назначению")

        return "\n".join(recommendations) if recommendations else "Критических issues не обнаружено"


def real_estate_checker():
    """Проверка правового режима недвижимости"""
    print("🏠 ПРОВЕРКА ПРАВОВОГО РЕЖИМА НЕДВИЖИМОСТИ")
    print("=" * 50)

    checker = RealEstateChecker()

    # Ввод кадастрового номера
    cadastral = input("Введите кадастровый номер (формат: XX:XX:XXXXXX:XXX): ").strip()

    if not checker.validate_cadastral_number(cadastral):
        print("Ошибка: Неверный формат кадастрового номера!")
        print("Пример правильного формата: 77:01:0001015:123")
        return

    checker.cadastral_number = cadastral

    print("\n🔍 Запрос данных из Росреестра...")

    # Проверка всех аспектов
    ownership = checker.check_ownership()
    if 'error' in ownership:
        print(f"Ошибка: {ownership['error']}")
        return

    checker.check_encumbrances()
    checker.check_vri()

    # Формирование и вывод отчета
    report = checker.generate_report()
    print(report)

    # Сохранение отчета
    filename = f"отчет_недвижимость_{cadastral.replace(':', '_')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Отчет сохранен в файл: {filename}")


# Запуск проверки
if __name__ == "__main__":
    real_estate_checker()