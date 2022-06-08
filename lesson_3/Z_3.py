"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
data = [random.randint(1, 100) for i in range(10)]
max = 0
min = 100
print(data)
for i in data:
    max = i if max < i else max
    min = i if min > i else min
spam = data.index(min)
data[data.index(max)] = min
data[spam] = max
print(data)

