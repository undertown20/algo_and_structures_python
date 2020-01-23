# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

profit = 0
enterprise_quality = 4
enterprise_info = namedtuple("enterprise", "name profit")
enterprise_list = []

for i in range(enterprise_quality):
  name_c = input("enterprise name: ")
  year = [int(i) for i in input(f'Пожалуйста, введите прибыль компании за 4 квартала {name_c}').split(' ')]
  enterprise = enterprise_info(name=name_c, profit=sum(year))
  enterprise_list.append(enterprise)

for i in enterprise_list:
  profit += i.profit
  profit = profit/enterprise_quality

print(f'Средняя прибыль для всех предприятий: {profit}')
print(f'Предприятия с прибылью выше среднего {[i for i in enterprise_list if i.profit > profit]}')
print(f'Предприятия с прибылью ниже среднего {[i for i in enterprise_list if i.profit < profit]}')

