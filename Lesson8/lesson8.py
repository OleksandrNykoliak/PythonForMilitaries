import logging
from math import log
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# def function(*args, **kwargs):

#     return [i for i in args if i % 2 == 0], kwargs


# print(function(1,2,3,4,5,6,7,8,9,10, age=20, city='Lviv', country='Ukraine', phone='1234567890'))

# def function1():
#     def function2():
#         print('function2')
#     function2()
# function1()

# def decorator(function):
#     def wrapper():
#         result = function() # hello
#         vowels = ['a', 'e', 'i', 'o', 'u']

#         for i in result: # пройшлись по слові hello
#             if i in vowels: # пройшлись по голосних літерах
#                 result = result.replace(i, i.upper())

#         return result
#     return wrapper


# @decorator
# def function():
#     return 'hello'


# print(function()) # hEllO


# decorator which takes a function as an argument and will return function with changed arguments

# def decoratorDB(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return result
#     return wrapper


# @decoratorDB
# def connection(database):
#     return f"Connected to the {database}"


# print(connection('PostgreSQL'))


# customers = {
#     'customer1': {
#         'name': 'Oleksandr',
#         'age': 20,
#         'city': 'Lviv',
#         'country': 'Ukraine',
#         'phone': '1234567890'
#     },
#     'customer2': {
#         'name': 'Ivan',
#         'age': 30,
#         'city': 'Kyiv',
#         'country': 'Ukraine',
#         'phone': '1234567890'
#     },
# }

# def BankOperation(customer=None, operation=None, amount=None):
#     if operation == 'поповнити':
#         return f"Клієнт {customer} поповнив рахунок на {amount} гривень"
#     elif operation == 'зняти':
#         return f"Клієнт {customer} зняв з рахунку {amount} гривень"
#     else:
#         return 'Вибачте, ви не вказали операцію'


# print(BankOperation(customer=customers['customer1'], operation='поповнити', amount=1000))


# def even_or_odd(number):
#     return 'Even' if number % 2 == 0 else 'Odd'


# def even_or_odd(number):
# 	return 'Odd' if number % 2 else 'Even'


# print(even_or_odd(5)) # Even

# def even_or_odd(number):
#   return ["Even", "Odd"][number % 2]
#         # ["Even", "Odd"][0]

# print(["Even", "Odd"][0])

# print(even_or_odd(10)) # Even


# avto_park = []


# def GermanyCarsDecorator(function):
#     def wrapper(*args):
#         result = function(*args)
#         germany_cars = [car for car in result if car == 'BMW' or car == 'Mersedes' or car == 'Audi']
#         print(f'Germany cars: {germany_cars}')
#         logging.info('Germany cars were printed')
#     return wrapper

# @GermanyCarsDecorator
# def function(*args):
#     avto_park.extend(args)
#     logging.info('New cars were added to the avto_park')
#     avto_park.sort()
#     logging.info('The avto_park was sorted')
#     try:
#         print(10 / 0)
#     except ZeroDivisionError:
#         logging.error('ZeroDivisionError')

#     print(avto_park)
#     logging.info('The avto_park was printed')

#     filtered_cars = list(filter(lambda car: car.startswith('B'), avto_park))
#     print(filtered_cars)

# function('BMW', 'Mersedes', 'Audi', 'Toyota', 'Ford', 'Pagani', 'Aston Martin', 'Bentley',
#          'Rolls Royce', 'Jaguar', 'Land Rover', 'Volvo', 'Saab', 'Scania', 'Volvo Trucks')


# def function_connection(database):
#     try:
#         connect = mongoDbConnection(database)
#         logging.info('Connected to the cloud database')
#         return connect
#     except Exception as e:
#         connect = LocalDB(database)
#         logging.info('Connected to the local database')
#         return 'Connected to the local database'

#     fi


# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     logging.error('ZeroDivisionError')
# finally:
#     raise Exception('наша видумана помилка')


# cars = ['Aston Martin', 'Audi', 'BMW', 'Bentley', 'Ford', 'Jaguar', 'Land Rover', 'Mersedes', 'Pagani', 'Rolls Royce', 'Saab', 'Scania', 'Toyota', 'Volvo', 'Volvo Trucks']

# # filter cars which starts with 'B'

# filtered_cars = list(filter(lambda car: car.startswith('B'), cars))

# print(list(filter(lambda number: number % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))

# lambda hello: hello + ' world'
# print((lambda hello: hello + ' world')('hello'))


# def calculator(a, b, operation):
#     operations = {
#         'add': lambda a, b: a + b,
#         'sub': lambda a, b: a - b,
#         'mul': lambda a, b: a * b,
#         'div': lambda a, b: a / b,
#         'pow': lambda a, b: a ** b,
#     }

#     return f"Гарно написана стрінга: {operations[operation](a, b)}"


# print(calculator(10, 5, 'add'))


# def function(number):
#     return 'Odd' if number % 2 else 'Even'

# lambda number: 'Odd' if number % 2 else 'Even'

# print((lambda number: 'Odd' if number % 2 else 'Even')(10))


# def farengeit(celsius):
#     return (celsius * 9/5) + 32

# lambda celsius: (celsius * 9/5) + 32


# def function(my_list):
#     return lambda: list(set([i for i in my_list if i % 2 == 0]))


# print(function([1,2,3,2,5,6,7,6,5,4,5,6,7,1,2,3,2])())


# def get_grade(s1, s2, s3):
#     score = sum([s1, s2, s3])
#     return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'


# def get_grade(*s):
#     return 'FFFFFFDCBAA'[sum(s)//30]


# print(get_grade(100, 5, 10)) # A


# print('FFFFFFDCBAA'[300//30]) # A

# from actual_data import *

# def weather(weatherToday):
#     result = f'The weather is {weatherToday} today'
#     return result

# print(weather(weatherToday))

# print(a)


# def function(parametr, text):
#    colors = {
#         'PURPLE': '\033[95m',
#         'CYAN': '\033[96m',
#         'DARKCYAN': '\033[36m',
#         'BLUE': '\033[94m',
#         'GREEN': '\033[92m',
#         'YELLOW': '\033[93m',
#         'RED': '\033[91m',
#         'BOLD': '\033[1m',
#         'UNDERLINE': '\033[4m',
#         'END': '\033[0m' }

#    print(colors[parametr] + text + colors[parametr])


# function('BOLD', 'якийсь текст')
# function('PURPLE', 'якийсь текст')
# function('CYAN', 'якийсь текст')
# function('UNDERLINE', 'якийсь текст')
# function('END', 'якийсь текст')
# function('GREEN', 'якийсь текст')


# colors = {
#     'PURPLE': '\033[95m',
#     'CYAN': '\033[96m',
#     'DARKCYAN': '\033[36m',
#     'BLUE': '\033[94m',
#     'GREEN': '\033[92m',
#     'YELLOW': '\033[93m',
#     'RED': '\033[91m',
#     'BOLD': '\033[1m',
#     'UNDERLINE': '\033[4m',
#     'END': '\033[0m'
# }

# def color_decorator(color):  # Decorator now takes a color parameter
#     def decorator(function):
#         def wrapper(*args, **kwargs):  # Use *args and **kwargs to accept an arbitrary number of arguments
#             color_code = colors.get(color, '')  # Safely get the color code, defaulting to empty string if not found
#             end_code = colors['END'] if color_code else ''  # Only add end code if a color code was found
#             result = function(*args, **kwargs)  # Call the original function
#             return f"{color_code}{result}{end_code}"  # Return the colored result
#         return wrapper
#     return decorator

# @color_decorator('RED')  # Specify the color as a decorator parameter
# def hello_world(text):
#     return text

# print(hello_world('hello world'))
