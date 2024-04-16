class SchoolStudy:
    def __init__(self) -> None:
        pass
    
    def Registration(self):
        print('Registration')
        
    def Division(self):
        print('Division')
        
    def Education(self):
        print('Education')
        
    def Schedule(self):
        print('Schedule') # Розклад
        
    def Subjects(self):
        print('Subjects') # Предмети
        
    def Teachers(self):
        print('Teachers') # Вчителі
        
    def Practise(self):
        print('Practise')
    
    
class Facade:
    def __init__(self):
        self.school = SchoolStudy()
        
    def some_methods_school(self):
        self.schedule = self.school.Schedule()
        self.subject = self.school.Subjects()
        self.teachers = self.school.Teachers()
     
             
facade = Facade()

facade.some_methods_school()