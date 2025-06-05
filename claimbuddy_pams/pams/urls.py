from django.urls import path
from . import views

app_name = 'pams'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
]