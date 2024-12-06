from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.EmailField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    shipping_depto = models.CharField(max_length=255, blank=True, null=True) 
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255, blank=True, null=True)
    shipping_zip_code = models.CharField(max_length=10, blank=True, null=True)
    shipping_country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f'Shipping Address for {self.shipping_full_name}'
