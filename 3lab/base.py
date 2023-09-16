""" Написать функцию, которая принимает целочисленный
список, состоящий из n элементов, и с помощью генераторного
выражения создает и возвращает список, элементами которого
являются удвоенные элементы входящего списка"""

h = []


def task4():
    def generator(x):
        for k in range(len(x)):
            yield x[::2]

    print('Введите числа для списка (Для окончания записи напишите букву k)')

    while True:
        u = input()
        if u == 'k':
            break
        else:
            h.append(int(u))

    list_after = generator(h)
    print(next(list_after))


task4()
