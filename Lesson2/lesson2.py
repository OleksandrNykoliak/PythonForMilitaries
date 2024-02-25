import copy

a = 10
b = 10.5
c = "Hello"
d = True
e = False
f = None
# змінний незмінний
# впорядкований не впорядкований
# індексований неіндексований


my_list = [1, 2, 3, 4, 5]
# змінний тип даних
# впорядкований
# індексований
print(my_list)

name = []
name.append("Sofia")  # додавання елементу в кінець списку
print(name)
name.append("Volodymyr")

# name = ['Sofia', 'Volodymyr']


name.insert(0, "Ivan")  # додавання елементу на позицію
print(name)

# name = ['Ivan', 'Sofia', 'Volodymyr']

name.insert(2, 'Petro')
print(name)

# ['Ivan', 'Sofia', 'Petro', 'Volodymyr']

name.remove('Ivan')  # видалення елементу
print(name)

# ['Sofia', 'Petro', 'Volodymyr']

name.pop(0)  # видалення елементу по індексу
print(name)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.pop()  # видалення останнього елементу
print(a)


name.clear()  # очищення списку
print(name)

# del name # видалення списку


y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = y.copy()  # копіювання списку

print(x)


a1 = [1, 2, 3, 4, 5]
print(a1.count(5))  # підрахувати кількість елементів в списку

a2 = [6, 8]

a2.extend(a1)  # додавання елементів списку
print(a2)


d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

d.extend(f)

print(d)


a1 = [1, 2, 33333]
a2 = []

a2.extend(a1)

a3 = []
a3.extend(a2)

print(a3)


a = [100]

b = a.copy()  # 100

a.append(200)  # 100, 200

print(a)  # 100, 200

print(b)  # 100


a = [1000000]

b = a.copy()

print(a is b)
print(id(a))
print(id(b))

print(a == b)


a = [1, 2, 3, 4, 5]
b = a.copy()
a.append(10)
print(a)


a = [1, 2, 3, [4, 5]]
b = copy.copy(a)

a[0] = 10
a[3].append(6)

print(a)  # Output: [10, 2, 3, [4, 5, 6]]
print(b)  # Output: [1, 2, 3, [4, 5, 6]] (shallow copy)


a = [1, 2, 3, [4, 5]]

# Deep copy example
c = copy.deepcopy(a)
a[3].append(6)
a[0] = 100


print(a)  # Output: [100, 2, 3, [4, 5, 6]]
print(c)  # Output: [1, 2, 3, [4, 5]]


a = [1, 2, 3, 4, 5]
b = [1, 1, 1]

print(a == b)


f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f.index(5))  # повертає індекс елементу в списку


f = [1, 2, 1, 2, 3, 4, 5, 4, 3, 2, 3]
f.sort(reverse=True)

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d.reverse()
print(d)


f = [9.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10.5, 0.5]

f.sort(key=int)
print(f)


name = 'Sofia'

print('Тут ми вивели слово: ', name)


a = [1, 2, 3, 4, 5]
a.sort()
b = sorted(a)


a = [1, 2, 1, 2, 3, 2, 1, 2, 3]

a.reverse()  # [3, 2, 1, 2, 3, 2, 1, 2, 1]

b = list(reversed(a))  # [1,2,1,2,3,2,1,2,3]
