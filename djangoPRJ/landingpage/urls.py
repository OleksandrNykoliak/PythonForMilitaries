from django.urls import path
from .views import RegistrationPageView, HomePageView, List_of_all_cars, RegisterCarView


urlpatterns = [
    path('registration/', RegistrationPageView.as_view(), name='registration'),
    path('home/', HomePageView.as_view(), name='home'),
    path('list_of_all_cars/', List_of_all_cars.as_view(), name='home'),
    path('register_car/', RegisterCarView.as_view(), name='register_car'),
]
