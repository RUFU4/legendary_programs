"""Написать функцию, которая принимает список, состоящий из n элементов, и возвращает их сумму"""

x = []


def task4():
    def summa(h):
        p = 0
        for k in range(0, len(h)):
            p = p + h[k]
        return p

    print('Введите числа для списка (Для окончания записи напишите букву k)')

    while True:
        u = input()
        if u == 'k':
            break
        else:
            x.append(int(u))
    print(summa(x))

task4()
