import sqlite3

"""Написать функцию, которая принимает наименование
таблицы и список списков, которые содержат данные, и обновляет данные полученной таблицы на указанные во внутренних
списках, где в качестве идентификаторов записей следует принимать
номер внутреннего списка плюс единица,
т.к. идентификаторы записей СУБД нумеруются с единицы"""

values = [
    ['Митяй', 'Потухший'],
    ['Феофан', 'Русич'],
    ['Святослав', 'Большерот']
]


def conn_and_replace(name, value):
    connection = sqlite3.connect('lab6.db')
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM""" + ' ' + name)
    cursor.executemany("""INSERT INTO""" + ' ' + name + ' ' +
                       """VALUES(NULL, ?, ?)""", value)

    connection.commit()
    connection.close()


conn_and_replace(input("Введите название таблицы \n"), values)
