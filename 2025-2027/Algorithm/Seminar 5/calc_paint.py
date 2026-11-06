def calc_paint():
    # Ввод данных
    length = float(input("Длина комнаты (м): "))
    width = float(input("Ширина комнаты (м): "))
    height = float(input("Высота комнаты (м): "))
    windows = float(input("Площадь окон и дверей (м²): "))

    # Вычисления
    walls_area = 2 * (length + width) * height
    paintable_area = walls_area - windows
    paint_liters = paintable_area / 10
    cans = round(paint_liters / 5)  # банки по 5 литров

    # Вывод результатов
    print(f"\nПлощадь стен: {walls_area:.1f} м²")
    print(f"Площадь для покраски: {paintable_area:.1f} м²")
    print(f"Необходимо краски: {paint_liters:.1f} литров")
    print(f"Рекомендуется банок: {cans} шт. по 5 литров")

calc_paint()