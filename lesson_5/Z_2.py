from collections import deque

hex_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

list_a = deque(input('Введите первое шеснадцетеричное значение: ').strip())
list_b = deque(input('Введите второе шеснадцетеричное значение: ').strip())
while len(list_a) < len(list_b): # Вставляем недостающие нули для сравнивания количества цифр в числах
    list_a.appendleft('0')
while len(list_b) < len(list_a):
    list_b.appendleft('0')

for i in list_a: # Переводим в 10 систему
    list_a[list_a.index(i)] = hex_dic[i]
for i in list_b:
    list_b[list_b.index(i)] = hex_dic[i]

list_sum = deque(map(lambda x, y: x + y, list_a, list_b))  #Складываем значения
"""
К сожалению, для реализации умножения не осталось времени (Не успеваю перевести результат
умножения к следующему шагу со сложением, нет идей...)
def mul(list_a, list_b):
    list_mul_s1 = deque()
    list_mul_s2 = deque()
    for i in list_a:                        #Перемножаем числа
        for j in list_b:
            list_mul_s1.append(i * j)
    print(list_mul_s1)
    if list_mul_s1[0] == 0:                 #Обрезаем лишние нули, которые были для сравнивания
        list_mul_s1 = deque(list_mul_s1, maxlen = (len(list_mul_s1) - len(list_a)))
    for i in range(1, len(list_a)):         #Попытка разделить результат умножения на слогаемые для перевода их в 16 систему
        list_mul_s2.append(deque(list_mul_s1, maxlen = (len(list_mul_s1) - len(list_a))*i)) 
        print(list_mul_s2)                  #Затор, как очередь значений разделить на несколко, с шагом в разряд?
    print(list_mul_s1)
mul(list_a,list_b)
"""

list_sum.reverse()
list_sum.extend('0000')
list_sum = deque(map(int, list_sum))

for i in list_sum: # Переводим в 16 систему
    if i < 16:
        list_sum[list_sum.index(i)] = hex_dic[i]
    else:
        spam = i // 16
        list_sum[list_sum.index(i)+1] += spam
        list_sum[list_sum.index(i)] = hex_dic[i-16]

list_sum.reverse()
spam = 0
for i in list_sum:
    if i == '0':
        spam +=1
    else:
        break
result = deque(list_sum, maxlen=len(list_sum)-spam)
print(result)

