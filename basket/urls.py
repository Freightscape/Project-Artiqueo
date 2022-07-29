from django.urls import path

from .import views

urlspatterns = [
    path('', views.basket_summary, name='basket_summary')
]