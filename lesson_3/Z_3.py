"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random, timeit, cProfile
data = [random.randint(1, 100) for i in range(10)]
#print(data)
def main(max, min):
    for i in data:
        max = i if max < i else max
        min = i if min > i else min
    spam = data.index(min)
    data[data.index(max)] = min
    data[spam] = max
    return data
#print(main(0, 100))

#cProfile.run('main(0, 100)')
#1    0.000    0.000    0.000    0.000 Z_3.py:7(main)
# "Z_3.main(0,100)"
# 1000 loops, best of 5: 671 nsec per loop
