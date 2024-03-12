# def helloWorld():
#     return 'Hello World'


# b = helloWorld()

# print(b)


# def printName(name):
#     return f"Hello, {name}!"


# print(printName('Roman'))
# print(printName('Sofia'))
# print(printName('Oleksandr'))


# def kvadrat_ploshcha(storona):
#     return f"Площа квадрата зі стороною {storona} дорівнює {storona ** 2}"

# print(kvadrat_ploshcha(5))
# print(kvadrat_ploshcha(8))


# def teorem_pifagora(katet1, katet2):
#     result = (katet1 ** 2 + katet2 ** 2) ** 0.5
#     return f"Гіпотенуза трикутника з катетами {katet1} та {katet2} дорівнює {result}"

# print(teorem_pifagora(4, 5))


# math, string, json, datatime, random, os, sys, re,
# requests, time, sqlite3, csv, pandas, numpy, matplotlib,
# seaborn, sklearn, tensorflow, keras, pytorch, django, flask, fastapi,
# aiohttp, pytest, unittest, selenium, beautifulsoup, scrapy


# from math import isqrt as korin

# print(korin(25))


# def function(name): # parameter
#     return f"Hello, {name}!"


# print(function('Roman')) # argument


# def function(a,b,c,d,e):
#     return sum([a,b,c,d,e])


# print(function(1,2,3,4,5))


# name = {
#     'name': 'Oleksandr',
#     'university': 'Lviv Polytechnic National University',
#     'faculty': 'Computer Science',
#     'year': 2012,
#     'lastname': 'Kovalchuk'
# }

# print(name.get('lastname', 'Not found'))


# def function(name=None, age=None):
#     return f"INFO: {name} \nAGE: {age}"

# print(function('Alex'))


# name = 'Oleksandr'
# age = 20

# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')
# print(f'Hello, my name is {name} and I am {age} years old')
# print('Hello, my name is {} and I am {} years old'.format(name, age))


# def function(*args): * arguments
#     return args

# print(function(1,2,3,4,5,6,7,8,9,101,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1))


# def function(**kwargs): # key:word arguments
#     return kwargs

# print(function(name='Oleksandr', age=20, city='Lviv', country='Ukraine', phone='1234567890'))

# def MongoDb():
#     print('MongoDb')

# def function(*args, **kwargs):
#     return args, kwargs


# print(function(1,2,3,4,5,6,7,8,9,10, age=20, city='Lviv', country='Ukraine', phone='1234567890'))


# def function(list1, list2):
#     list1.extend(list2)
#     return list(set([i for i in list1 if i % 2 == 0]))


# print(function([1,2,3,2,5,6,7,6,5,4,5,6,7,1,2,3,2], [1,2,18,7,8,7,6,2,3,2,1,2,3]))


# 1 відсіємо дублікати
# посортуємо
# створимо новий список знепарними елементами


# dollar_to_gryvna = 39
# euro_to_gryvna = 42


# я мушу сказати шо я хочу зробити, продати чи купити
# я  мушу сказати валюту


# dollar_to_gryvna = 25
# euro_to_gryvna = 42


# def MoneyExchange(whatToDo, valiuta, amount=1.0):
#     operations = {
#         'продати': 'Продаємо',
#         'купити': 'Купляємо'
#     }
#     current_currency = {
#         'dollar': dollar_to_gryvna,
#         'euro': euro_to_gryvna
#     }

#     if not whatToDo:
#         return 'Вибачте, ви не вказали операцію'
#     if not valiuta:
#         return 'Вибачте, ви не вказали валюту'
#     if valiuta == 'dollar':
#         return f"{operations[whatToDo]} {amount} доларів за {amount * current_currency['dollar']} гривень"
#     elif valiuta == 'euro':
#         return f"{operations[whatToDo]} {amount} євро за {amount * current_currency['euro']} гривень"


# print(MoneyExchange('продати', 'dollar', 300))


# def function(range_of_numbers: list = 'пусто'):
#     def helloWorld():
#         def helloWorld1():
#             return 'BATMAN'
#         return helloWorld1()
#     return helloWorld()

# print(function([1,1,1,1,1,1]))





# x = []

# for i in  range(1, 101):
#     x.append(i)
    
# print(x)  

# x = [i for i in range(1, 101) if i % 2 == 0]  

# print(x)



# Зробіть список з алфавіту англійського || a = [i for i in alphabet]
# Зробіть список з голосних літер
# підніміть всі літери в верхній регістр
# переверніть список

import string 


alphabet = string.ascii_lowercase


a = [bukva.upper() for bukva in reversed(alphabet) if bukva in 'aouei']

print(a)
