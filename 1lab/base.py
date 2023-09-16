h1 = []
h2 = []
x = []
y = []


def inputik(x, y):
    p = [x[1], y[1]]
    return p


print('Введиите значения для двух списков по-очереди')

for k in range(3):
    u = input()
    h1.append(u)
    u = None

for k in range(3):
    u = input()
    h2.append(u)
    u = None

print(inputik(h1, h2))