"""
Author: Elijah Kinyanjui
(c) Copyright by HugosLabs ltd

File: 
Description: 


"""
from django.urls import path
from . import views

urlpatterns = [
     path('home', views.home, name="home"),
     path('', views.items, name="item_list"),
     path('item_kits', views.items, name="item_kits"),
     path('edit/<int:pk>', views.UpdateItemView.as_view(), name="update_items")
]