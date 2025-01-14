from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    # path('update/', views.update, name='update'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    # path('update_customer/', views.update_customer, name='update_customer'),
    path('product/<int:id>', views.product, name='product'),
    path('category/<str:slug>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
]