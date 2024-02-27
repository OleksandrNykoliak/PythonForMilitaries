
# mutable vs immutable

# множина   змінний, неупорядкований, неіндексований, не має дублікатів
from datetime import date
import datetime


my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# списки  змінний, впорядкований, індексований, може містити дублікати
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# кортеж  незмінний, впорядкований, індексований, може містити дублікати
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# словник  змінний, індексований, не має дублікатів
my_dict = {'a': 1, 'b': 2, 'c': 3}


w = 1
x = 1.0
y = "1"
z = True
complex_c = 1 + 1j
t_byte = b"1"
t_byte_array = bytearray(10)


# print()
# type()
# id()
# len()
# hash()
# input()
# copy()

# import string
# import math
# import random
# import datetime
# import json

# print(type('[{hello world}]'))

# print('10')

# person = {
#     "name": "Sofia",
#     "age": 20,
#     "city": "Lviv",
# }


# import json

# file = json.dumps(person)

# print(type(file))

# with open('data.json', 'w') as f:
#     f.write(file)


# counter = 0
# while counter < 10:
#     print('hello')
#     counter = counter + 1


# names = ['Sofia', 'Ivan', 'Oleh', 'Ira', 'Oksana']

# names = iter(names)
# print(next(names))
# print(next(names))
# print(next(names))
# print(next(names))
# print(next(names))
# print(next(names))


# e = []

# for i in range(1, 1001):
#     e.append(i)


# e = [i for i in range(1, 1001)]


# names = ['Sofia', 'Ivan', 'Oleh', 'Ira', 'Oksana']

# vowels = ['a', 'e', 'i', 'o', 'u']

# filtered_names = [''.join([letter for letter in name if letter.lower() in vowels]) for name in names]

# print(filtered_names)  # ['oia', 'Ia', 'e', 'Ia', 'Oaa']


# validated_names = [name.upper() for name in names if name[-1] == 'a']

# print(validated_names)
