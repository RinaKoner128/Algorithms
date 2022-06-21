"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""
import random, timeit, cProfile
def main(size):
    data = [random.randint(-100, 100) for i in range(size)]
    max = -100
#    print(data)
    for i in data:
        if i < 0:
            max = i if max < i else max
#    print(f'Максимальный отрицательный элемент {max} находится на {data.index(max)} позиции')
    return max, data.index(max)

#cProfile.run('main(20)')
# 1    0.000    0.000    0.000    0.000 Z_5.py:6(main)
# 1    0.000    0.000    0.000    0.000 Z_5.py:7(<listcomp>)
# "Z_5.main(20)"
# 1000 loops, best of 5: 12.4 usec per loop
# "Z_5.main(50)"
# 1000 loops, best of 5: 30 usec per loop
# "Z_5.main(100)"
# 1000 loops, best of 5: 59.5 usec per loop


