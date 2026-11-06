def download_time_calculator():
    """Расчет времени загрузки файла"""
    file_size = float(input("Размер файла (МБ): "))
    download_speed = float(input("Скорость интернета (Мбит/с): "))

    # Конвертация Мбит/с в МБ/с (1 байт = 8 бит)
    speed_mb_per_sec = download_speed / 8
    time_seconds = file_size / speed_mb_per_sec

    # Преобразование в часы, минуты, секунды
    hours = int(time_seconds // 3600)
    minutes = int((time_seconds % 3600) // 60)
    seconds = int(time_seconds % 60)

    print(f"Время загрузки: {hours}ч {minutes}мин {seconds}сек")


download_time_calculator()