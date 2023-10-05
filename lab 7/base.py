"""Написать класс, который содержит два метода
«get_string» и «print_upper_string», где первый метод
принимает строку, а второй выводит данную строку в верхнем регистре"""


class Trasform:

    def __init__(self):
        self.string = None

    def getstring(self, text):
        self.string = text

    def print_upper_string(self):
        print(self.string.upper())


transformobj = Trasform()
transformobj.getstring(str(input()))
transformobj.print_upper_string()
