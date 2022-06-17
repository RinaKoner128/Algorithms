'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный
массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
'''
import random
def bubble_sort(lst):
    n = 1
    while n < len(lst):
        count = 0
        for i in range(len(lst) - 1 - (n - 1)):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
        if count == 0:
            break
        n += 1

data = [random.randint(-100, 100) for i in range(10)]
print(data)
bubble_sort(data)
print(data)