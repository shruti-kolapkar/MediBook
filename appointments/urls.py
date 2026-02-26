from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('book/<int:id>/', views.book_appointment, name='book'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
]