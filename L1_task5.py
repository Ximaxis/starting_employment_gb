"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную
функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день
каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит
в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
"""

offer = ({'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
         {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
         {'begin_sum': 100000, 'end_sum': 1000001, 6: 7, 12: 8, 24: 7.5}
         )


def deposit(sum_deposit, delta_time, sub_deposit):
    if delta_time not in (6, 12, 24):
        return False
    for single_offer in offer:
        if sum_deposit in range(single_offer['begin_sum'], single_offer['end_sum']):

            for month in range(1, delta_time + 1):
                current_sub_deposit = 0
                if month != 1 or month != delta_time:
                    current_sub_deposit = sub_deposit

                time_rate = single_offer[delta_time] / 12
                sum_deposit += current_sub_deposit + ((sum_deposit + current_sub_deposit) * time_rate / 100)
            return sum_deposit
    return False


my_money = deposit(10000, 24, 100)
if my_money is False:
    print("Была допущена ошибка в данных")
else:
    print(round(my_money, 2))

