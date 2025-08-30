import time

while True:
    print('Зеленый постоянный')
    time.sleep(3)
    for i in range(3):
        print('Зеленый мигающий')
        time.sleep(1)
    print('Желтый постоянный')
    time.sleep(3)
    print('Красный постоянный')
    time.sleep(3)
