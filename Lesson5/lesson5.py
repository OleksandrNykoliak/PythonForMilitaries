# a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# first_length = sum(a[0] // len(a[0]))

# sum = 0
# for elements in a:
#     for element in elements:
#         sum += element
#         print(sum//len(elements))


# a = [(1, 2), (2, 3), (3, 4)]

# v = []

# for elements in a:
#     element = list(elements)
#     print(element)

# for i in a:
#     v.append(list(i))
# print(v)

# v = [list(i) for i in a]


# my_list = [3, 1, -2]

# your_list = [3, 1, -2]

# # t = my_list[-1]

# print(my_list[-2])

# print(my_list[my_list[-1]])


# LEGB
# Local, Enclosing, Global, Built-in


# print(str(int(float(10))))


# a = []
# for i in range(-1, 2):
#     a.append(i)

# print(len(a))


# print([i for i in range(1, 10)])


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# b = ('hello',)

# print(type(b))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# b = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
# c = {1, 2, 3, 4, 5, 6, 7, 8, 9, (1, 2, 3, 4, 5, 6, 7, 8, 9)}


# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     2.0 : 5
# }

# print(d[5])
# # print(d.get('a'))


# student = {
#     'name': 'John',
#     'age': 25,
#     'courses': ['Math', 'CompSci'],
#     'graduated': False,
#     'parents': {
#         'father': 'Mike',
#         'mother': 'Jane'
#     }
# }

# print(student['parents']['father'])


# student = {
#     1: {
#         'name': 'John',
#         'age': 25,
#         'courses': ['Math', 'CompSci'],
#         'graduated': False,
#         'parents': {
#             'father': 'Mike',
#             'mother': 'Jane'
#         },
#     },
#     2: {
#         'name': 'John',
#         'age': 25,
#         'courses': ['Math', 'CompSci'],
#         'graduated': False,
#         'parents': {
#             'father': 'Mike',
#             'mother': 'Jane'
#         }
#     },
#     3: {
#         'name': 'John',
#         'age': 25,
#         'courses': ['Math', 'CompSci'],
#         'graduated': False,
#         'parents': {
#             'father': 'Mike',
#             'mother': 'Jane'
#         },
#     }
# }


# my_dict = {
#     'name': 'Roman',
#     'age': 25,
#     'city': 'Lviv'
#     }


# my_dict.update({'test': 'test'})
# print(my_dict)
# # my_dict.clear()
# my_dict.pop('test')
# print(my_dict)
# my_dict.popitem()
# print(my_dict)
# # a = my_dict.copy()


# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# names = ['John', 'Paul', 'George', 'Ringo']
# sallary = 10000

# a = dict.fromkeys(names, sallary)
# print(a)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # x = car.items()

# # print(x)

# print(car.values())


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model", "Bronco")

# print(x)

# student = {
#     'name': 'IVAN',
#     # 'lastname' : 'IVANOV',
# }

# lastname = student.setdefault('lastname', 'Тут немає значення')
# print(lastname)


# city = {
#     'name': 'Lviv',
#     'population': 1000000,
# }

# city['population'] = 800000
# print(city)


# print(city.get('country', 'Тут немає значення')) # setdefault


# r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r.remove(15)
# r.discard(15)


# a = [i for i in range(1, 10)]

# a = []
# for i in range(1, 10):
#     a.append(i)

# list comprehension
# tuple comprehension
# set comprehension
# dictionary comprehension


# import string
# alphabet = string.ascii_lowercase

# mydict = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }

# my_dict = {key: value for key, value in zip(range(1, len(alphabet) + 1), alphabet)}


# for key, value in my_dict.items():
#     print(key, value)

# for key in my_dict.keys():
#     print(key)

# for element in my_dict.values():
#     print(element)


# import json

# not_validated = []


# with open('data.json') as f:
#     data = json.load(f)

#     for element in data:
#         if '@' not in element['email']:
#             not_validated.append(element['first_name'])

#     with open('not_validated.txt', 'w') as f:
#         for name in not_validated:
#             f.write(name + '\n)'+ '100')


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : {
#             "name" : "Emil",
#             "year" : 2004
#             },

#   "child2" : {
#             "name" : "Tobias",
#             "year" : 2007},
#   "child3" : {
#             "name" : "Linus",
#             "year" : 2011
#   }
# }


# student = dict(name='Alex', age=29, city='Lviv')

# student1 = {
#     'name': 'Oleksandr',
#     'age': 29,
#     'city': 'Lviv'
# }

# print(student)
# print(student1)


# g = {key: value for key, value in zip(range(1, 51), reversed(range(1, 51)))}


# print(g)


# blocks = int(input('введіть скільки блоків має бути: '))
# height = 0
# layer = 1

# while layer <= blocks:
#     height += 1
#     blocks -= layer
#     layer += 1

# print(f'Висота нашої піраміди {height} поверхи')


# """
# Якщо дохід громадянина не перевищував 85 528 доларів, податок дорівнював 18% від доходу мінус 556 доларів і
# 2 центи (це була так звана податкова пільга)

# якщо дохід був вищий за цю суму, податок дорівнював 14 839 доларів і 2 центи плюс 32% надлишку понад 85 528 доларів.

# """

# sallary = int(input('введіть скільки ви заробили за цей рік: '))

# if sallary <= 85528:
#     tax = sallary * .18 - 556.02
# elif sallary > 85528:
#     tax = 14839.02 + ((sallary - 85528) * .32)


# print(f'Податок який ви маєте заплатити: {tax}')
