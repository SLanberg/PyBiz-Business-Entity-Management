from django.urls import path
from . import views

urlpatterns = [
    path('establish', views.create_limited_liability_company, name='establish_company'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
]
