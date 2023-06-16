# Функция enumerate()
# применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.

# Вывести [(0, 'user1'), (1, 'user2'), (2, 'user3))]

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)