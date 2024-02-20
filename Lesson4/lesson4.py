# a = 10

# myCar = 'BMW'
# MyCar = 'Audi'
# my_car = 'Mersedes'

# MYCAR = 'Toyota'


# # Застосуйте copy.copy до списку a і змініть вкладений список, потім виведіть обидва списки.
# import copy

# a = [1, 2, [3, 4]]
# b = copy.copy(a)
# b[2][0] = 5

# print(a)
# print(b)

# print('-------------------')

# # Створіть глибоку копію списку a за допомогою copy.deepcopy і виведіть обидва списки після змін.
# a = [1, 2, [3, 4]]
# b = copy.deepcopy(a)
# b[2][0] = 5

# print(a)
# print(b)


# a = [1,2,3,3,3,33,[1,11,111]]


# my_tuple = (1, 2, 3, 3, 3, 3, 3, 3, 3, True, False,
#             2.0, 'dfkjsdofjd')  # кортеж, tuple

# print(my_tuple.index(3))  # повертає індекс першого входження елемента
# print(my_tuple.count(3))  # повертає кількість входжень елемента

# a = {
#     923067657514726816: 8765432345678765434567,
# }

# print(a['age'])

# a = list(a)
# print(type(a))
# a.append('Ми додали вкінець кортежу елемент')
# a = tuple(a)
# print(type(a))
# print(a)

# h = 8765432345678765434567  # 923067657514726816
# print(hash(h))


# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2

# print(id(tuple1))


# Компіляція програми - перетворення коду в байт-код .pyc файл
# Інтерпретація програми - виконання коду рядок за рядком, 101010101010101 перетворення в binary code
# id - повертає унікальний ідентифікатор об'єкта в пам'яті

# GIL - Global Interpreter Lock - це механізм, який забезпечує, що в один момент часу тільки один потік має доступ
# до інтерпретатора Python.


# Zen python - це документ, який описує філософію Python, написаний Тімом Пітерсом.
# print zen

# import this


# list()
# tuple()

# set() # множина, набір

# # !!!

# a = {1,2,3,[1,2,3], (1,2,3), 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, True, False, 2.0, 'dfkjsdofjd'}

# print(a)

# колекція яку можна змінювати
# сет не має порядкової структури
# сет не має дублікатів
# сет не має індексації
# сет не може всередині мати змінних типів даних


# fruits = {"apple", "banana", "cherry"}

# fruits.add("orange") # додає елемент в множину

# print(fruits)


# fruits = {"apple", "banana", "cherry"}

# fruits.clear() # очищає множину

# print(fruits)


# fruits = {"apple", "banana", "cherry"}

# x = fruits.copy() # копіює множину

# print(x)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}


# z = x.difference(y) # повертає різницю множин x і y banana cherry
# print(z)


# h = y.difference(x) # повертає різницю множин x і y google microsoft
# print(h)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.difference_update(y)  # {'banana', 'cherry'}
# print(x)

# y.difference_update(x)  # {'google', 'microsoft'}
# print(y)


# r = {"apple", "banana", "cherry"}

# r.remove("banana")

# r.discard("bla bla bla")


# x = {"apple", "banana", "cherry"}

# y = {"google", "microsoft", "apple"}

# z = x.intersection(y) # повертає спільні елементи множин x і y apple
# h = y.intersection(x) # повертає спільні елементи множин x і y apple

# print(h)


# x = {"apple", "banana", "cherry"}
# print(id(x))
# y = {"google", "microsoft", "apple"}

# print('-------------------після змін')
# x.intersection_update(y)
# print(id(x))

# # y.intersection_update(x)

# print(x)


# x = {"apple", "banana", "cherry", "microsoft"}
# y = {"google", "microsoft", "facebook"}

# z = x.isdisjoint(y) # повертає True якщо немає спільних елементів

# print(z)

# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}

# z = y.issubset(x)

# print(z)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.update(y) # додає елементи множини y в множину x

# print(x)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y) # повертає об'єднання множин x і y і присвоює його змінній z

# print(z)




# text = 'TENET'
    

# print(text == text[::-1])

# print(text == ''.join(reversed(text)))


# def square_digits(num):
#     return int(''.join(str(int(i)**2) for i in str(num)))
    
# print(square_digits(9119))  # 811181