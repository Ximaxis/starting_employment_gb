import os


def print_directory_contents(path):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами
    """
    cur_dir_list = os.listdir(path)

    for item in cur_dir_list:
        path_to_child = os.path.join(path, item)

        if os.path.isfile(path_to_child):
            print(path, item)
        if os.path.isdir(path_to_child):
            print_directory_contents(path_to_child)


print_directory_contents(os.getcwd())
