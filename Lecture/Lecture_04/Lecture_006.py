# Функция map() 
# применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.

data = '1 2 3 5 8 15 23 38'

data = list(map(int, data.split()))

print(data)