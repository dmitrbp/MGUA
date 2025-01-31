import os

def create_directory_and_write_files(directory_path, file_prefix):
    """
    Создает директорию и записывает в нее 10 файлов.
    :param directory_path: Имя директории
    :param file_prefix: Префикс имени файлов, которые будут записаны в директории.
    """
    try:
        # Создаем директорию, если ее еще нет
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Директория '{directory_path}' успешно создана.")
        else:
            print(f"Директория '{directory_path}' уже существует.")

        # Путь к файлу
        file_prefix_path = os.path.join(directory_path, file_prefix)

        # Записываем файлы
        for suffix in range(10):
            file_path = file_prefix_path + str(suffix)
            file_content = f'I am file number {suffix}'
            with open(file_path, 'w') as file:
                file.write(file_content)
                print(f"Файл '{file_path}' успешно записан в директорию '{directory_path}'.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Задаем параметры
directory_path = 'tempdir'
file_prefix = 'file_number_'

create_directory_and_write_files(directory_path, file_prefix)
