"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа
'0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""
import sys
def show_sizeof(x, level=0):
    print ('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        elif not isinstance(x, str) :
            for xx in x:
                show_sizeof(xx, level + 1)
def v1():
    while True:
        mark = str(input('Введите операцию, которую хотите совершить: "+, -, *, /" или 0 (если хотите выйти из программы): '))
        if mark != '+' and mark != '-' and mark != '*' and mark != '/' and mark != '0':
            mark = input('Введено некорректное значение оператора. Выберите операцию из предложенных: ')
        if mark == '0':
            print('Программа завершена')
            break

        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

        if mark == '+':
            result = a + b
            print(f'{a} + {b} = {result}')
        elif mark == '-':
            result = a - b
            print(f'{a} - {b} = {result}')
        elif mark == '*':
            result = a * b
            print(f'{a} * {b} = {result}')
        elif mark == '/':
            try:
                result = a / b
                print(f'{a} / {b} = {result}')
            except ZeroDivisionError:
                b = int(input('На "0" делить нельзя. Введите иной делитель: '))
                result = a / b
                print(f'{a} / {b} = {result}')
        print(show_sizeof(a))
        print(show_sizeof(b))
        print(show_sizeof(mark))
        print(show_sizeof(result))
def v2():
    while True:
        user_input = [input('Введите операцию, которую хотите совершить: "+, -, *, /" или 0 (если хотите выйти из программы): '),
                      int(input('Введите первое число: ')),
                      int(input('Введите второе число: '))]
        if user_input[0] != '+' and user_input[0] != '-' and user_input[0] != '*' and user_input[0] != '/' and user_input[0] != '0':
            user_input[0] = input('Введено некорректное значение оператора. Выберите операцию из предложенных: ')
        if user_input[0] == '0':
            print('Программа завершена')
            break

        if user_input[0] == '+':
            user_input.append(user_input[1] + user_input[2])
            print(f'{user_input[1]} + {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '-':
            user_input.append(user_input[1] - user_input[2])
            print(f'{user_input[1]} - {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '*':
            user_input.append(user_input[1] * user_input[2])
            print(f'{user_input[1]} * {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '/':
            try:
                user_input.append(user_input[1] / user_input[2])
                print(f'{user_input[1]} / {user_input[2]} = {user_input[3]}')
            except ZeroDivisionError:
                user_input[2] = int(input('На "0" делить нельзя. Введите иной делитель: '))
                user_input.append(user_input[1] / user_input[2])
                print(f'{user_input[1]} / {user_input[2]} = {user_input[3]}')
        print(show_sizeof(user_input))
def v3():
    list_mark = ['*', '/', '-', '+', '0']
    while True:
        user_input = [input('Введите операцию, которую хотите совершить: "+, -, *, /" или 0 (если хотите выйти из программы): '),
                      int(input('Введите первое число: ')),
                      int(input('Введите второе число: '))]
        if list_mark.count(user_input[0]) == 0:
            user_input[0] = input('Введено некорректное значение оператора. Выберите операцию из предложенных: ')
        if user_input[0] == '0':
            print('Программа завершена')
            break

        if user_input[0] == '+':
            user_input.append(user_input[1] + user_input[2])
            print(f'{user_input[1]} + {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '-':
            user_input.append(user_input[1] - user_input[2])
            print(f'{user_input[1]} - {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '*':
            user_input.append(user_input[1] * user_input[2])
            print(f'{user_input[1]} * {user_input[2]} = {user_input[3]}')
        elif user_input[0] == '/':
            try:
                user_input.append(user_input[1] / user_input[2])
                print(f'{user_input[1]} / {user_input[2]} = {user_input[3]}')
            except ZeroDivisionError:
                user_input[2] = int(input('На "0" делить нельзя. Введите иной делитель: '))
                user_input.append(user_input[1] / user_input[2])
                print(f'{user_input[1]} / {user_input[2]} = {user_input[3]}')
        print(show_sizeof(user_input))
        print(show_sizeof(list_mark))
v1()
v2()
v3()

# Версия и разрядность ОС и интерпретатора Python:
#3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] win32

#v1:
#  type = <class 'int'>, size = 28, object = 256
#  type = <class 'int'>, size = 28, object = 164
#  type = <class 'str'>, size = 50, object = *
#  type = <class 'int'>, size = 28, object = 41984

# type = <class 'int'>, size = 28, object = 2
# type = <class 'int'>, size = 28, object = 1
# type = <class 'str'>, size = 50, object = -
# type = <class 'int'>, size = 28, object = 1

#v2
#type = <class 'list'>, size = 120, object =['*', 7, 4, 28]
#type = <class 'list'>, size = 120, object = ['-', 2, 1, 1]

#v3
#type = <class 'list'>, size = 120, object = ['*', 256, 164, 41984]
#type = <class 'list'>, size = 120, object = ['*', '/', '-', '+', '0']

"""
Вывод: Самый оптимальный вариант оказалось использовать список для хранения 
переменных, от пользователя. Но возникает несущественная логическая несязанность - 
проверка того, что пользователь ввел неверный знак (не '0', '+', '-', '', '/'),
откладывается на время,после ввода всех данных пользователем.
Первый вариант существенно существенно тяжелее по памяти, но есть возможность сразу 
проверять правильность вводимых данных.
"""