from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index')
]