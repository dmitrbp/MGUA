import re
from datetime import datetime
import json


class ContractRiskAnalyzer:
    def __init__(self):
        self.risk_keywords = {
            'неустойка': {
                'level': 'высокий',
                'description': 'Проверьте размер неустойки на соответствие ст. 333 ГК РФ',
                'recommendation': 'Убедитесь, что размер неустойки соразмерен возможным убыткам',
                'context_keywords': ['процент', 'день просрочки', 'штраф', 'пеня']
            },
            'форс-мажор': {
                'level': 'средний',
                'description': 'Проверьте перечень обстоятельств непреодолимой силы',
                'recommendation': 'Убедитесь, что перечень не является излишне узким',
                'context_keywords': ['обстоятельства', 'непреодолимая сила', 'освобождение']
            },
            'конфиденциальность': {
                'level': 'средний',
                'description': 'Проверьте определение конфиденциальной информации',
                'recommendation': 'Четко определите, какие сведения являются конфиденциальными',
                'context_keywords': ['информация', 'разглашение', 'тайна']
            },
            'арбитражный суд': {
                'level': 'низкий',
                'description': 'Проверьте подсудность споров',
                'recommendation': 'Убедитесь, что подсудность соответствует законодательству',
                'context_keywords': ['споры', 'разрешение', 'подсудность']
            },
            'убытки': {
                'level': 'высокий',
                'description': 'Проверьте условия возмещения убытков',
                'recommendation': 'Внимательно изучите clauses, ограничивающие возмещение убытков',
                'context_keywords': ['возмещение', 'ограничение', 'ответственность']
            },
            'безвозмездно': {
                'level': 'высокий',
                'description': 'Риск переквалификации в договор дарения',
                'recommendation': 'Для коммерческих организаций избегайте безвозмездных условий',
                'context_keywords': ['дарение', 'бесплатно', 'без оплаты']
            },
            'гарантия': {
                'level': 'средний',
                'description': 'Проверьте условия гарантийных обязательств',
                'recommendation': 'Уточните сроки и объем гарантийных обязательств',
                'context_keywords': ['качество', 'срок гарантии', 'обязательства']
            }
        }

    def preprocess_text(self, text):
        """Предобработка текста для анализа"""
        # Приводим к нижнему регистру и удаляем лишние пробелы
        text = text.lower().strip()
        # Заменяем множественные пробелы на одинарные
        text = re.sub(r'\s+', ' ', text)
        return text

    def find_risk_context(self, text, keyword, context_words=5):
        """Поиск контекста вокруг риск-слова"""
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = []

        for match in pattern.finditer(text):
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            context = text[start:end]
            # Выделяем ключевое слово
            highlighted_context = context.replace(keyword, f'**{keyword.upper()}**')
            matches.append(highlighted_context)

        return matches

    def analyze_contract(self, contract_text):
        """Основной метод анализа договора"""
        # Предобработка текста
        processed_text = self.preprocess_text(contract_text)

        found_risks = {}

        # Поиск риск-слов в тексте
        for keyword, risk_info in self.risk_keywords.items():
            if re.search(r'\b' + re.escape(keyword) + r'\b', processed_text):
                # Найдено риск-слово, анализируем контекст
                contexts = self.find_risk_context(processed_text, keyword)

                # Проверяем наличие контекстных ключевых слов
                context_analysis = []
                for context_word in risk_info['context_keywords']:
                    if context_word in processed_text:
                        context_analysis.append(context_word)

                found_risks[keyword] = {
                    'level': risk_info['level'],
                    'description': risk_info['description'],
                    'recommendation': risk_info['recommendation'],
                    'contexts': contexts,
                    'related_contexts': context_analysis,
                    'context_found': len(context_analysis) > 0
                }

        return found_risks

    def generate_report(self, found_risks, contract_name=""):
        """Генерация отчета по найденным рискам"""
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

        report = f"""
        ОТЧЕТ О ПРОВЕРКЕ ДОГОВОРА НА РИСКИ
        ==================================
        Договор: {contract_name or 'Не указан'}
        Дата проверки: {timestamp}
        Всего найдено рисков: {len(found_risks)}

        """

        # Группируем риски по уровням
        high_risks = {k: v for k, v in found_risks.items() if v['level'] == 'высокий'}
        medium_risks = {k: v for k, v in found_risks.items() if v['level'] == 'средний'}
        low_risks = {k: v for k, v in found_risks.items() if v['level'] == 'низкий'}

        # Добавляем риски по уровням
        if high_risks:
            report += "\n🚨 ВЫСОКИЙ УРОВЕНЬ РИСКА:\n" + "=" * 40 + "\n"
            for keyword, risk in high_risks.items():
                report += self._format_risk(keyword, risk)

        if medium_risks:
            report += "\n⚠️  СРЕДНИЙ УРОВЕНЬ РИСКА:\n" + "=" * 40 + "\n"
            for keyword, risk in medium_risks.items():
                report += self._format_risk(keyword, risk)

        if low_risks:
            report += "\nℹ️  НИЗКИЙ УРОВЕНЬ РИСКА:\n" + "=" * 40 + "\n"
            for keyword, risk in low_risks.items():
                report += self._format_risk(keyword, risk)

        # Сводная статистика
        report += f"""
        СВОДНАЯ СТАТИСТИКА:
        ------------------
        Всего рисков: {len(found_risks)}
        Высокий риск: {len(high_risks)}
        Средний риск: {len(medium_risks)}
        Низкий риск: {len(low_risks)}

        РЕКОМЕНДАЦИИ:
        -------------
        {self._generate_overall_recommendations(found_risks)}
        """

        return report

    def _format_risk(self, keyword, risk):
        """Форматирование информации о риске"""
        risk_text = f"""
        РИСК: {keyword.upper()}
        Уровень: {risk['level'].upper()}
        Описание: {risk['description']}
        Рекомендация: {risk['recommendation']}
        """

        if risk['contexts']:
            risk_text += "        Контекст:\n"
            for i, context in enumerate(risk['contexts'][:2], 1):  # Показываем первые 2 контекста
                risk_text += f"          {i}. ...{context}...\n"

        if risk['related_contexts']:
            risk_text += f"        Связанные термины: {', '.join(risk['related_contexts'])}\n"

        risk_text += "\n" + "-" * 50 + "\n"
        return risk_text

    def _generate_overall_recommendations(self, found_risks):
        """Генерация общих рекомендаций"""
        if not found_risks:
            return "Критических рисков не обнаружено. Рекомендуется проверить договор на соответствие внутренним регламентам."

        recommendations = []

        if any(risk['level'] == 'высокий' for risk in found_risks.values()):
            recommendations.append("Обнаружены риски высокого уровня! Требуется срочный пересмотр указанных условий.")

        if 'неустойка' in found_risks:
            recommendations.append("Проверить размер неустойки на соразмерность (ст. 333 ГК РФ).")

        if 'безвозмездно' in found_risks:
            recommendations.append("Исключить безвозмездные условия для избежания переквалификации в дарение.")

        if 'форс-мажор' in found_risks:
            recommendations.append("Расширить перечень форс-мажорных обстоятельств.")

        return "\n        ".join(recommendations) if recommendations else "Риски требуют внимательного изучения."


def main():
    """Основная функция программы"""
    print("🔍 АНАЛИЗАТОР ДОГОВОРОВ НА ЮРИДИЧЕСКИЕ РИСКИ")
    print("=" * 60)

    analyzer = ContractRiskAnalyzer()

    # Пример договора для анализа
    sample_contract = """
    ДОГОВОР ПОСТАВКИ № 123/П
    г. Москва «01» сентября 2023 г.

    ООО «Поставщик», именуемое в дальнейшем «Поставщик», с одной стороны, и
    ООО «Покупатель», именуемое в дальнейшем «Покупатель», с другой стороны,
    заключили настоящий договор о нижеследующем:

    1. ПРЕДМЕТ ДОГОВОРА
    Поставщик обязуется поставить Товар, а Покупатель обязуется принять и оплатить его.

    2. ПОРЯДОК РАСЧЕТОВ
    Оплата производится в течение 10 банковских дней с момента поставки.
    За просрочку оплаты Покупатель уплачивает НЕУСТОЙКУ в размере 1% от суммы долга за каждый день просрочки.

    3. ОТВЕТСТВЕННОСТЬ СТОРОН
    Стороны освобождаются от ответственности при наступлении обстоятельств непреодолимой силы (ФОРС-МАЖОР).
    Возмещение УБЫТКОВ ограничивается суммой договора.

    4. КОНФИДЕНЦИАЛЬНОСТЬ
    Условия настоящего Договора являются конфиденциальной информацией.

    5. РАЗРЕШЕНИЕ СПОРОВ
    Все споры подлежат разрешению в Арбитражном суде города Москвы.

    6. ПРОЧИЕ УСЛОВИЯ
    Поставка товара осуществляется на БЕЗВОЗМЕЗДНОЙ основе в рамках акции.
    """

    print("1. Анализ примерного договора")
    print("2. Ввод своего текста договора")
    print("3. Загрузка из файла")

    choice = input("\nВыберите вариант (1-3): ").strip()

    if choice == "1":
        contract_text = sample_contract
        contract_name = "Пример договора поставки"
    elif choice == "2":
        print("Введите текст договора (Ctrl+D для завершения ввода):")
        contract_text = ""
        try:
            while True:
                line = input()
                contract_text += line + "\n"
        except EOFError:
            pass
        contract_name = "Введенный договор"
    elif choice == "3":
        filename = input("Введите имя файла: ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                contract_text = f.read()
            contract_name = filename
        except FileNotFoundError:
            print("Файл не найден! Используется примерный договор.")
            contract_text = sample_contract
            contract_name = "Пример договора поставки"
    else:
        print("Используется примерный договор.")
        contract_text = sample_contract
        contract_name = "Пример договора поставки"

    # Анализ договора
    print(f"\n🔍 Анализ договора: {contract_name}")
    found_risks = analyzer.analyze_contract(contract_text)

    # Генерация и вывод отчета
    report = analyzer.generate_report(found_risks, contract_name)
    print(report)

    # Сохранение отчета в файл
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"отчет_риски_{timestamp}.txt"

    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Отчет сохранен в файл: {report_filename}")

    # Дополнительно: сохранение в JSON для машинной обработки
    json_data = {
        'contract_name': contract_name,
        'analysis_date': datetime.now().isoformat(),
        'total_risks': len(found_risks),
        'risks': found_risks
    }

    json_filename = f"риски_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"📊 Данные сохранены в JSON: {json_filename}")


if __name__ == "__main__":
    main()