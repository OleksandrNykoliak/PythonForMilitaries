from django.db import models



class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.model
    
    
class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cars = models.ManyToManyField(Car)
    
    def __str__(self):
        return self.name