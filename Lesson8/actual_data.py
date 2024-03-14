
weatherToday = 'GREAT'


a = 1000


def color_decorator(function):              # тут декоратор приймає функцію
    
    def wrapper(other_number):                             # ми створили обгортку, яка відповідає 
        
        return f"{function('TEST')}, {function(other_number)}"     # структурі функції, яку ми плануємо змінювати
      
    return wrapper                                                 # повернули функцію обгортку, яка вернула кінцевий результат
 
