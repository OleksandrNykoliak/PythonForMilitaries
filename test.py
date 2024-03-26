def clean():
    print('Cleaning up')
    print('Done')
    
def cook():
    print('Cooking')
    print('Done')
    
def eat():
    print('Eating')
    print('Done')
    
    
class HomeStaff:
    def __init__(self, name):
        self.name = name
        self.clean()
        self.cook()
        self.eat()
        
    def clean(self):
        clean()
        
    def cook(self):
        cook()
        
    def eat(self):
        eat()
        
        
a = HomeStaff()