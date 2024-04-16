# facade_example.py

class Drive:
    def drive_ferrari(self):
        print("Drive Ferrari")
        
    def drive_lamborghini(self):
        print("Drive Lamborghini")
    
    def drive_mercedes(self):
        print("Drive Mercedes")
        
    def drive_bmw(self):
        print("Drive BMW")
        
    def drive_tesla(self):
        print("Drive Tesla")
        
    def drive_nissan_leaf(self):
        print("Drive Nissan Leaf")
        
    def repair_ferrari(self):
        print("Repair Ferrari")
    
    def repair_lamborghini(self):
        print("Repair Lamborghini")
        
    def repair_tesla(self):
        print("Repair Tesla")
        
    def repair_nissan_leaf(self):
        print("Repair Nissan Leaf")
        
    def unique_drive(self):
        print("Unique Drive from Drive class")
        
        
class FacadeElectroCars:
    def __init__(self):
        self.drive = Drive()
        
    def drive_electro_cars(self):
        self.drive.drive_tesla()
        self.drive.drive_nissan_leaf()
        
    def repair_electro_cars(self):
        self.drive.repair_tesla()
        self.drive.repair_nissan_leaf()
        
        
        
class UniqueDrive:
    def __init__(self):
        self.drive = Drive()
        
    def unique_drive(self):
        self.drive.unique_drive()
        


test1 = UniqueDrive()

test1.unique_drive()