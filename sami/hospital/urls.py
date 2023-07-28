from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('register-patient',views.RegisterPatient,name='register-patient'),
    path('register-doctor',views.RegisterDoctor,name='register-doctor'),
    path('nurse',views.Nurse,name='Nurse'),
    path('add-drug', views.add_drug, name='add-drug'),
    path('doctor/<int:pk>',views.Doctor,name='doctor'),
]