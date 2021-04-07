"""
Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется
процентная ставка: 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб
(6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию, в которую будут
передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть представлен в
виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала и конца диапазона суммы
вклада и значения процентной ставки для каждого срока. В функции необходимо проверять принадлежность суммы вклада к
одному из диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
"""
offer = ({'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
         {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
         {'begin_sum': 100000, 'end_sum': 1000001, 6: 7, 12: 8, 24: 7.5}
         )


def deposit(sum_deposit, delta_time):
    if delta_time not in (6, 12, 24):
        return False
    for single_offer in offer:
        if sum_deposit in range(single_offer['begin_sum'], single_offer['end_sum']):
            for month in range(delta_time):
                time_rate = single_offer[delta_time]/12
                sum_deposit += (sum_deposit * time_rate / 100)
            return sum_deposit
    return False


my_money = deposit(10000, 24)
if my_money is False:
    print("Была допущена ошибка в данных")
else:
    print(round(my_money, 2))
