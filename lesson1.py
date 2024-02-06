
print('Hello world')

""" Якийсь коментар для вашого коду
вждіьваждівьаждвіьа
івжадьівждаьвіа
іважьівждаьів
іваьль
"""

print(1+1)
print(1-1)
print(1*1)
print(3**3)
print(10/2)
print(10//4)

def function(name):
    """ Ця функція видруковує
    імя користувача """
    print(name)


function('Oleksandr')


a = 10
b = 15
print(a+b)

a = 11
b = 15
print(a+b)


a = b = c = d = f = 100

print(a==b==c==f)


b = 50

print(a)

a = 'text'

print(id(a)) # 93897768838040

print(hash(a)) # -6103626717625161344


a = 10  # <class 'int'> integer, ціле число
b = 15.5 # <class 'float'> float, дробове число число з крапкою
c = 'some text' # <class 'str'>, string текст строка рядок
d = True # <class bool>, булевий або логічний тип даних, істина або неістина
f = False  # <class bool>, булевий або логічний тип даних, істина або неістина
e = None # <class 'NoneType'>
int()
float()
str()
bool()

a = 'text'
b = "text"

a = bool(1)
b = bool(0)

print(a > b)

print(True > False)

print(bool(1))
print(bool(0))


print('Sofia' > 'Maryana')

print(bool('Sofia'))
print(bool('Maryana'))


print()
type(1)
len('text')


t = 'a             bcdefgh'

counter = 0

for i in t:
    if i == ' ':
        counter = counter + 1


print(counter)


a = 10
print(type(a))

print('____________тут ми поміняли тип')

a = float(a)
print(a)
print(type(a))


print(type(e))

= - знак присвоєння
# == - знак перевірки на рівність

print(10 == 10) # зараз я стверджую
print(10 == 12) # зараз я стверджую
print(10 != 12) # зараз я стверджую що 10 не дорівнює 12
print(10 < 12) # зараз я стверджую
print(10 > 12) # зараз я стверджую
print(10 >= 12) # зараз я стверджую
print(10 <= 12) # зараз я стверджую


a = True
while a:
    print('hello')
