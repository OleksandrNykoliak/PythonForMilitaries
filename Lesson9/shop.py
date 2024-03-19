
# class Customer:
#     def __init__(self, name,phone, balance, list_of_products=[]):
#         self.name = name
#         self.phone = phone
#         self.balance = balance
#         self.list_of_products = list_of_products 
        
#     def buy_product(self, product, price):
#         self.list_of_products.append(product)
#         self.balance -= price
#         return self.list_of_products
    
#     def return_product(self, product, price):
#         self.list_of_products.remove(product)
#         self.balance += price
#         return self.list_of_products
    
#     def show_balance(self):
#         print(f'{self.name} balance is {self.balance}')
         
#     def __str__(self):
#         return f'Name: {self.name},\nPhone: {self.phone},\nBalance: {self.balance},\nList of products: {self.list_of_products}'
        
# class Shop:
#     def __init__(self, name, adress, products=[], dayly_income=0):
#         self.name = name
#         self.adress = adress
#         self.products = products
#         self.dayly_income = dayly_income
    
#     def __str__(self) -> str:
#         return f'Shop name: {self.name},\nAdress: {self.adress},\nProducts: {self.products},\nDayly income: {self.dayly_income}'

# roman = Customer('Roman', '380638878882', 2500)
# arsen = Shop('Arsen', 'Lviv, Shevchenka 100',['apple', 'banana', 'orange'], 0)

# print(roman.buy_product('apple', 100))
# print(roman.buy_product('banana', 200))
# print(roman.buy_product('orange', 300))
# roman.show_balance()


# class Phone:
#     def __init__(self, phone_number, balance, owner):
#         self.phone_number = phone_number
#         self.balance = balance
#         self.owner = owner
        
#     def left24Hours(self):
#         self.balance -= 10
#         print(f'You have left {self.balance} hrn')
        
#     def recharge(self, amount):
#         self.balance += amount
#         print(f'You have recharged your phone on {amount} hrn')
            
#     def __str__(self):
#         return f'Phone number: {self.phone_number},\nBalance: {self.balance},\nOwner: {self.owner}'
    

# RomanNykoliak536263 = Phone('380638878882', 100, 'Roman')

# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()
# RomanNykoliak536263.left24Hours()

# RomanNykoliak536263.recharge(500)

# print(RomanNykoliak536263)




