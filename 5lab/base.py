"""Написать функцию, которая принимает путь к файлу,
текст и номер строки и записывает в файл полученный текст в
указанный номер строки. """


def task4():
    def find_paste(link, texti, number):
        f = open(link, 'w+', encoding="utf-8")
        try:
            i = 0
            while i < number:
                f.write("\n")
                i = i + 1
            f.write(texti)
        except IOError:
            print("Указан неверный путь")
        finally:
            f.close()

    print("Введите путь к файлу, номер строки и текст")
    while True:
        file_link = str(input())
        string_number = int(input())
        text = str(input())
        break

    find_paste(file_link, text, string_number)


task4()
