# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

s = input('Введите шестизначное число: ')

if len(s) == 6:
    a = int(s[0]) + int(s[1]) + int(s[2])
    b = int(s[3]) + int(s[4]) + int(s[5])
    if (a == b):
        print('Yes')
    else:
        print('No')
else:
    print('Требуется ввести шестизначное число!')