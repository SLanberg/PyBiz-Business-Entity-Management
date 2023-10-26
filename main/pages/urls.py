from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('establish', views.create_limited_liability_company, name='establish_company'),
    path('company_list', views.company_list, name='company_list'),
]
