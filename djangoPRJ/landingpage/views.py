from calendar import c
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .models import Car

from .models import Car

class RegistrationPageView(TemplateView):
    template_name = 'registration.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
class List_of_all_cars(TemplateView):
    template_name = 'list_of_all_cars.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context
    



class RegisterCarView(View):
    template_name = 'register_car.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        
        # Validate that all fields are provided
        if not model or not year or not price:
            return render(request, self.template_name)

        try:
            year = int(year)  # Ensure year is an integer
            price = float(price)  # Ensure price is a float
        except ValueError:
            return render(request, self.template_name)
        
        # Create and save the new car instance
        Car.objects.create(model=model, year=year, price=price)
        return redirect('home')  # Assuming 'list_of_all_cars' is a valid URL name

    