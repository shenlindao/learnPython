n = int(input('Введите расстояние, которое проходит авто за день: '))
m = int(input('Введите общий пробег: '))

res = (m + n - 1) // n
print(res)