"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random
data = [random.randint(1, 5) for i in range(15)]
count = 0
number = 0
print(data)
for i in data:
    if count < data.count(i):
        number = i
        count = data.count(i)
print(f'Число {number} встречается {count} раз.')