from turtle import home

from .import views

from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('cal/',views.calculate,name='calculate'),
]
