

class ConstructionCompany:
    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress
        self.employees_info = {}
        self.my_list_workers = []

    # avalon.hire_workers(worker1, 'Manager', 28000)

    def hire_workers(self, worker, position, sallary):
        self.employees_info[worker] = (position, sallary)
        try:
            worker.company = self.name
        except AttributeError:
            pass
        if isinstance(worker, Worker):
            self.my_list_workers.append(worker.name)
        else:
            self.my_list_workers.append(worker)

        return f'Ми найняли {worker} на посаду {position} зарплата {sallary}'

    def fire_workers(self, worker):
        self.workers_list.remove(worker)
        return f'Ми звільнили {worker}'

    def __str__(self) -> str:
        return f'Назва компанії: {self.name}, Адреса: {self.adress}, Телефон: {self.phone}, Список обєктів: {self.objects_list}, Список працівників: {self.workers_list}'


class Worker:
    def __init__(self, name: str = None, company: str = None, sallary: int = 0, position: str = None):
        self.name = name
        self.company = company
        self.sallary = sallary
        self.position = position

    def __str__(self) -> str:
        return f'Імя працівника: {self.name}, Компанія: {self.company}, Зарплата: {self.sallary}, Посада: {self.position}'


avalon = ConstructionCompany('Avalon', 'Lviv')
worker1 = Worker('Ivan')
avalon.hire_workers(worker1, 'Manager', 28000)
print(avalon.my_list_workers)


karpatbud = ConstructionCompany('Karpatbud', 'Kyiv')
worker2 = Worker('Petro')
karpatbud.hire_workers(worker2, 'Manager', 30000)
print(karpatbud.my_list_workers)


avalon.hire_workers(karpatbud.my_list_workers[0], 'Manager', 30000)
