try:
    file = open(".gitignore.txt", "r")
    content = file.read()
    file.close()
    print("Вміст файлу:", content)
except FileNotFoundError:
    print("Помилка: Файл не знайдено")