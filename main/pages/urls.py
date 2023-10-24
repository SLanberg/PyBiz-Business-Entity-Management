from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('establish', views.CompanyCreateView.as_view(), name='establish_company'),
    path('company-list', views.company_list, name='company_list'),
]
