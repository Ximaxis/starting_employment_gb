"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def generate_random(a, b):
    if a <= 0 or b <= 0:
        return print("Fail")
    list_generate = []
    dict_generate = {}
    for _ in range(10):
        random_number = random.randint(a, b)
        list_generate.append(random_number)

    for d in list_generate:
        dict_generate.update({f'elem_{list_generate.index(d)+1}': d})

    print(list_generate)
    print(dict_generate)


generate_random(8, 23)


