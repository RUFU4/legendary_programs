''' Написать функцию, которая принимает два целочисленных списка, содержащих по три элемента каждый,
и возвращает новый список, состоящий из двух элементов, являющихся средними во входящих списках.
Например, для следующих входящих списков {1,2,3} и {3,4,5} итоговым будет {2,4}'''


def task4():
    h1 = []
    h2 = []

    def middle_value(x, y):
        p = [x[1], y[1]]
        return p

    print('Введиите значения для двух списков по-очереди')

    for k in range(7):
        if k > 3:
            u = input()
            h2.append(u)
        elif k < 3:
            u = input()
            h1.append(u)

    print(middle_value(h1, h2))
    return

task4()