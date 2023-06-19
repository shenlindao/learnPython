# Функция map()
# Результат работы map() — это итератор. По итератору можно пробежаться только один раз. 
# Чтобы работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)