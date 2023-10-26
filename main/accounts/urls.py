from django.urls import path
from . import views

urlpatterns = [
    path('establish', views.create_limited_liability_company, name='establish_company'),
]
