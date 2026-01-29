# Юридическое основание: ст. 25.14-1 НК РФ
import datetime
from random import randint


def prepare_cfc_notification(taxpayer_id, cfc_name, cfc_country, ownership_percentage, financial_year):
    return {'number': randint(1, 100), 'name': cfc_name, 'country': cfc_country}


def submit_to_tax_authority(notification):
    number = randint(1, 100)
    submission_result = {
        'status': 'rejected', 'date': datetime.datetime, 'number': number
    }
    if number < 50:
        submission_result['status'] = 'accepted'
    return submission_result


def register_notification_submission(cfc_id, submission_date, notification_number):
    pass


def submit_cfc_notifications(taxpayer_id, year, list_of_cfcs):
    """
    Подача уведомлений о контролируемых иностранных компаниях.
    Количество итераций = количество КИК в списке.
    """
    notification_count = 0

    for index, cfc in enumerate(list_of_cfcs, start=1):
        # 1. Подготовить уведомление по форме КНД 1120092
        notification = prepare_cfc_notification(
            taxpayer_id=taxpayer_id,
            cfc_name=cfc['name'],
            cfc_country=cfc['country'],
            ownership_percentage=cfc['ownership'],
            financial_year=year
        )

        # 2. Подать уведомление в ФНС
        submission_result = submit_to_tax_authority(notification)

        # 3. Зарегистрировать факт подачи
        if submission_result['status'] == 'accepted':
            register_notification_submission(
                cfc_id=cfc['id'],
                submission_date=submission_result['date'],
                notification_number=submission_result['number']
            )
            notification_count += 1
            print(f"✅ Уведомление по КИК '{cfc['name']}' подано (№{index})")
        else:
            print(f"❌ Ошибка подачи уведомления по КИК '{cfc['name']}'")

    # 4. Проверить исполнение обязанности
    if notification_count == len(list_of_cfcs):
        print(f"Обязанность по уведомлению исполнена полностью. Подано: {notification_count} уведомлений.")
        return "complete"
    else:
        print(f"Внимание! Подано только {notification_count} из {len(list_of_cfcs)} уведомлений.")
        return "partial"


# Использование:
cfc_list = [
    {'id': 1, 'name': 'BlueSky Holdings Ltd', 'country': 'Кипр', 'ownership': 45},
    {'id': 2, 'name': 'Nordic Invest GmbH', 'country': 'Германия', 'ownership': 30},
    {'id': 3, 'name': 'Asia Trade Co.', 'country': 'Сингапур', 'ownership': 25}
]

result = submit_cfc_notifications(
    taxpayer_id="7701123456",
    year=2023,
    list_of_cfcs=cfc_list
)
