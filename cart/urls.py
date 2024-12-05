from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/', views.add_cart, name='add_cart'),
    path('remove/', views.remove_cart, name='remove_cart'),
    path('update/', views.update_cart, name='update_cart'),
]