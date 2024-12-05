from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, Customer, Order, Profile
from django.contrib.auth.models import User

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    model = User
    field = ['username', 'email']
    inlines = [ProfileInline]

if admin.site.is_registered(User):
    admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)