"""Написать функцию, которая принимает два вектора и
возвращает их внешнее произведение. """

import numpy

cor1 = []
cor2 = []


def vector_multiply(cora, corb):
    a = numpy.array(cora, dtype=float)
    b = numpy.array(corb, dtype=float)
    mult = numpy.outer(a, b)
    return mult


for k in range(4):
    print('Введите' + ' ' + str(k) + ' ' + 'кординату 1 и 2 вектора')
    cor1.append(int(input()))
    cor2.append(int(input()))

print('Результат\n')
print(vector_multiply(cor1, cor2))
