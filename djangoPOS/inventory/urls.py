"""
Author: Elijah Kinyanjui
(c) Copyright by HugosLabs ltd

File: 
Description: 


"""
from django.urls import path
from . import views

urlpatterns = [
     path('', views.items, name="item_list"),
     path('item_kits', views.items, name="item_kits"),
     path('categories', views.items, name="categories"),
     path('edit/<int:pk>', views.ItemUpdateView.as_view(), name="update_item"),
     path('pricing/<int:pk>', views.ItemPricingView.as_view(), name="item_pricing"),
     path('variations/<int:pk>', views.ItemPricingView.as_view(), name="item_variations"),
     path('images/<int:pk>', views.ItemPricingView.as_view(), name="item_images"),
     path('locations/<int:pk>', views.ItemPricingView.as_view(), name="item_locations"),
     path('create_item', views.ItemCreateView.as_view(), name="create_item")
]