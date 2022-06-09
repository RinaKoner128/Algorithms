"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random, timeit, cProfile
def main(size):
    count = 0
    number = 0
    data = [random.randint(1, 5) for i in range(size)]
#    print(data)
    for i in data:
        if count < data.count(i):
            number = i
            count = data.count(i)
#    print(f'Число {number} встречается {count} раз.')
    return count
#cProfile.run('main(15)')
# 1    0.000    0.000    0.000    0.000 Z_4.py:6(main)
# 1    0.000    0.000    0.000    0.000 Z_4.py:9(<listcomp>)
# "Z_4.main(15)"
# 1000 loops, best of 5: 11.8 usec per loop
# "Z_4.main(50)"
# 1000 loops, best of 5: 49.2 usec per loop
# "Z_4.main(100)"
# 1000 loops, best of 5: 130 usec per loop
