from django.contrib import admin

# Register your models here.
from .models import Car, Owner

admin.site.register(Car)
admin.site.register(Owner)