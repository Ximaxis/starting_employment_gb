"""
1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат
выполнения заданий 1 и 2 должен быть идентичным.
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции
тремя способами.
"""


class ItemDiscount:
    def __init__(self, product_name, price):
        self._product_name = product_name
        self._price = price

    def parent_price(self):
        return f'Цена в родительском {self._price}'


class ItemDiscountReport(ItemDiscount):
    def __init__(self, product_name, price, discount=0):
        super().__init__(product_name, price)
        self.discount = discount

    def get_parent_data(self):
        return f'{self._product_name} стоит {self._price}'

    def set_price(self, price):
        self._price = price

    def __str__(self):
        return f'{self._product_name} со скидкой стоит {self._price - self.discount}'


milk = ItemDiscountReport("Молоко", 50, 20)
milk.set_price(40)
print(milk.get_parent_data())
print(milk.parent_price())
print(milk)


class ItemPolimorfOne(ItemDiscount):
    def get_info(self):
        return print(self._product_name)


class ItemPolimorfTwo(ItemDiscount):
    def get_info(self):
        return print(self._price)


poli_one = ItemPolimorfOne("Хлеб", 45)
poli_two = ItemPolimorfTwo("Яйца", 90)

poli_one.get_info()
poli_two.get_info()

for obj in (poli_one, poli_two):
    obj.get_info()


def obj_info(obj):
    obj.get_info()


obj_info(poli_one)
obj_info(poli_two)
