from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile.objects.create(user=instance)
            user_profile.save()

    post_save.connect(create_profile, sender=User)



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/', blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')    
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.products
    
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create_and_save(name, email, phone=None, address=None):
        customer = Customer(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        customer.save()
        return customer
    
    @classmethod
    def get_by_email(cls, email):
        return cls.objects.filter(email=email).first()
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/categories/', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"