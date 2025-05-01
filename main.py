import os
from sys import exit

Exit = ""


def FileOpen():
    action = input(
        "Вы хотите прочесть файл или написать в нём что-то новое?\nВведите 'W' (Написать) или 'R' (Прочесть): ")
    print()
    if action == "r" or action == "R":
        file.seek(0)
        print(file.read())
    elif action == "w" or action == "W":
        data = input(f"Вы в файле {FileName} \nВы можете вводить текст!\n")
        file.write(data + "\n")
    else:
        print("Неизвестное Действие!")


while 1 > 0:
    print("\nДобро пожаловать в Редактор Текстовых Файлов!")
    FileName = input(
        "Введите название файла который вы хотите создать (если такой файл существует мы вас предупредим), Что-бы выйти напишите 'Exit': ")
    if FileName == "Exit" or FileName == "exit":
        exit(0)
    elif os.path.isfile(f"TextFiles/{FileName}.txt"):
        print("Данный файл существует!\n")
    else:
        print("Данный файл не существует, создаём новый файл...\n")

    file = open(f"TextFiles/{FileName}.txt", "a+", encoding="utf-8")

    FileOpen()

    file.close()
