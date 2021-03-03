from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create_read',views.create_read,name='createread'),
    path('delete_instance',views.delete_instance,name='deleteinstance'),
    path('update_instance',views.update_instance,name='updateinstance'),

]
