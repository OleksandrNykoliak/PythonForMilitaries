
price = {
    'hodova_diagnostika': 1000,
    'balance_of_wheels': 500,
    'paint': 2000,
    'electronic': 1500,
    'himchustca': 1000
}


class Service:
    def __init__(self, price: dict = None) -> None:
        self.price = price

    def hodova_diagnostika(self):
        print('Ми зробили найкращу діагностику вашого автомобіля')

    def balance_of_wheels(self):
        print('Ми зробили балансування коліс')

    def paint(self):
        print('Ми зробили фарбування автомобіля')

    def electronic(self):
        print('Ми зробили ремонт електроніки автомобіля')

    def himchustca(self):
        print('Ми зробили вам хімчистку салону')

    def total_price(self):
        total_price = sum(value for value in price.values())
        print(f'Вартість послуг: {total_price}')


class ServiceForEndUser:
    def __init__(self):
        self.service = Service()

    def make(self):
        self.service.hodova_diagnostika()
        self.service.balance_of_wheels()
        self.service.paint()

    def how_much(self):
        print(f'Вартість послуг: {self.service.total_price()}')


basic_diagnostic = ServiceForEndUser()

basic_diagnostic.how_much()
