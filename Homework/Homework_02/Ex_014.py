# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введи число N: '))
i = 0
while 2 ** i <= N:
    print(f' 2 в степени {i} = {2 ** i}')
    i += 1