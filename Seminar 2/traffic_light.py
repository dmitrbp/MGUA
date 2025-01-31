from time import sleep

while True:
	print('Зеленый постоянный')
	sleep(3)
	for i in range(3):
		print('Зеленый мигающий')
		sleep(1)
	print('Желтый постоянный')
	sleep(3)
	print('Красный постоянный')
	sleep(3)
	