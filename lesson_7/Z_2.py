'''
2. Отсортируйте по возрастанию методом слияния одномерный
вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random
def bose_nelson(data):
    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(j, m, m)
            j = j + m + m
        m = m + m
    return data

def bose_nelson_merge(j, r, m):
    if j + r < len(data):
        if m == 1:
            if data[j] > data[j + r]:
                data[j], data[j + r] = data[j + r], data[j]
        else:
            m = m // 2
            bose_nelson_merge(j, r, m)
            if j + r + m < len(data):
                bose_nelson_merge(j + m, r, m)
            bose_nelson_merge(j + m, r - m, m)
    return data

data = [random.randint(0, 50) for i in range(10)]
print(data)
bose_nelson(data)
print(data)