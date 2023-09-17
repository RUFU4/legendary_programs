from datetime import date

'''Написать функцию, которая принимает объект datetime
и возвращает номер недели.'''


def task4():
    def weeknumber(data):
        a = data.timetuple().tm_yday
        return int(a) // 7

    print("Введите полную дату, начиная с года\n")
    b = date(int(input()), int(input()), int(input()))
    print(weeknumber(b))


task4()
