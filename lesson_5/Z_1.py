"""
1.
"""

from collections import namedtuple, OrderedDict
import statistics

ave = 0
dic_comp = OrderedDict()
Company = namedtuple('Company', 'name profit1 profit2 profit3 profit4')
count = int(input('Введите количество предприятий: '))
for i in range(count):
    my_comp = Company(input('Введите название предприятия: '),
                      float(input(f'Введите прибыль за 1 квартал: ')),
                      float(input(f'Введите прибыль за 2 квартал: ')),
                      float(input(f'Введите прибыль за 3 квартал: ')),
                      float(input(f'Введите прибыль за 4 квартал: ')))
    dic_comp[my_comp] = (my_comp.profit1 + my_comp.profit2 + my_comp.profit3 + my_comp.profit4)
ave = statistics.mean(dic_comp.values())
print(f'Среднее значение: {ave}')
for i in dic_comp:
    if dic_comp[i] > ave:
        print(f'Компания {i.name}  заработала больше среднего ({dic_comp[i]})')
    elif dic_comp[i] < ave:
        print( f'Компания {i.name} заработала меньше среднего ({dic_comp[i]})')
    else: print( f'Компания {i.name} заработала средний уровень ({dic_comp[i]})')


