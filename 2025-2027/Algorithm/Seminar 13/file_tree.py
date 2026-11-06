# Допустим, у нас есть "дерево" папок
tree = [
    "file1.txt",
    ["folder1", "file2.txt", "file3.txt"],
    "file4.txt",
    ["folder2", ["subfolder", "file5.txt"], "file6.txt"]
]

def print_files(item, level=0):
    indent = "  " * level  # Отступ для красоты
    if isinstance(item, list):
        # Если это папка (список)
        print(f"{indent}[Папка]")
        for element in item:
            # РЕКУРСИЯ: вызываем функцию для содержимого папки
            print_files(element, level + 1)
    else:
        # Если это файл (строка)
        print(f"{indent}- {item}")

print_files(tree)