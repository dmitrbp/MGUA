def time_converter():
    """Преобразование общего количества секунд в формат ЧЧ:ММ:СС"""
    total_seconds = int(input("Введите количество секунд: "))

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"{total_seconds} секунд = {hours:02d}:{minutes:02d}:{seconds:02d}")


time_converter()