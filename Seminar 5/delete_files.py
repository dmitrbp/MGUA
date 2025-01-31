import os

def delete_files_in_directory(directory_path):
    """
    Удаляет все файлы в указанной директории.
    :param directory_path: Путь к директории, где нужно удалить файлы.
    """
    try:
        # Проверяем, существует ли директория
        if not os.path.exists(directory_path):
            print(f"Директория {directory_path} не существует.")
            return

        # Проходим по всем файлам в директории
        files = os.listdir(directory_path)
        while files:
            file_path = os.path.join(directory_path, files[0])
            # Удаляем только файлы, игнорируя подкаталоги
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Удален файл: {file_path}")
            files = os.listdir(directory_path)

        print("Все файлы в директории удалены.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Путь к директории, где нужно удалить файлы
directory = 'tempdir'
delete_files_in_directory(directory)
