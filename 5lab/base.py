"""Написать функцию, которая принимает путь к файлу,
текст и номер строки и записывает в файл полученный текст в
указанный номер строки. """


def task4():
    def find_paste(link, texti, number):
        try:
            f = open(link, 'r+', encoding="utf-8")
            string_value = f.readlines()
            string_value[number] = string_value[number] + texti
            print(string_value)
            f = open(link, 'w', encoding="utf-8")
            f.writelines(i for i in string_value)
            f.close()
        except IOError:
            print("Указан неверный путь")

    print("Введите путь к файлу, номер строки и текст")
    while True:
        file_link = str(input())
        string_number = int(input())
        text = str(input())
        break

    find_paste(file_link, text, string_number)


task4()
