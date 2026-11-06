from datetime import datetime, timedelta

def is_limitation_period_valid(violation_date):
    limitation_period = timedelta(days = 3 * 365)  # 3 года
    current_date = datetime.now().date()
    return current_date - violation_date <= limitation_period

# Пример использования
violation_date = datetime(2020, 5, 10).date()
print(is_limitation_period_valid(violation_date))  # False (если сейчас 2025 год)