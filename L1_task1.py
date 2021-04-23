"""
Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
"""


def multiplication_table(a, b):
    """
    Функция вывода таблицы умножения AxB
    :param a: первое входящее число
    :param b: второе входящее число
    :return: лист значений таблицы умножения
    """

    try:
        table = []
        for x in range(1, a+1):
            table_sub = []
            for y in range(1, b+1):
                table_sub.append(f"{x} x {y} = {x*y}")
            table.append(table_sub)
        return table
    except TypeError:
        print("Введены неверные значения")


table_final = multiplication_table(10, 10)
for row in table_final:
    for cell in row:
        print(cell, end='\t')
    print()


# Вариант 2 без отправки данных их функции
# def multiplication_table(a, b):
#     """
#     Функция вывода таблицы умножения AxB
#     :param a: первое входящее число
#     :param b: второе входящее число
#     """
#     try:
#         for x in range(1, a+1):
#             for y in range(1, b+1):
#                 print(f"{x} x {y} = {x*y}", end='\t')
#             print()
#     except TypeError:
#         print("Введены неверные значения")
#
#
# multiplication_table(10, 10)



