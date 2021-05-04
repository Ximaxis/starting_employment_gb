"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).

2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они
совпадают, программа должна возвращать значение True, иначе False.

3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.

4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл
с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка: с
текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка
файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный
файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа
должна запускаться по вызову первой функции.

5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод
первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех
подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
# 1
import re
import os
import random
import string


def name_file(path: str):
    return re.split(r'\.', re.split(r'/', path)[-1])[0]


print(name_file('../mainapp/views.py'))

# 2


def search_int(i):
    try:
        if '.' in i:
            float(i)
            print("Дробное")
        else:
            int(i)
            print("Целое число")
    except ValueError:
        print("Не является числом")


integer = input("Введите число")
search_int(integer)


# 3
def create_dictionary(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    return {key: value for (key, value) in zip(keys, values)}


print(create_dictionary([3, 4, 5, 6], [44, 66, 56]))


# 4

LENGTH = 10


def get_random_char():
    return random.choice(string.ascii_lowercase)


def get_random_string(length):
    random_list = [get_random_char() for i in range(length)]
    return ''.join(random_list)


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as file:
        numbers = [random.randint(0, 100) for _ in range(LENGTH)]
        strings = [get_random_string(LENGTH) for _ in range(LENGTH)]
        file.writelines([f'{number} {text}\n' for number, text in zip(numbers, strings)])
        return file


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            print(line)


descriptor = create_text_file('file.txt')
if descriptor:
    print_text_file(descriptor)

# 5

with open('file.txt', encoding='utf-8') as source_file:
    with open('new_file.txt', 'w', encoding='utf-8') as result_file:
        for line in source_file:
            text = re.findall(r'[a-z]+', line)[0]
            result_file.writelines(re.sub(r'\d+', text, line))
