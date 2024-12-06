from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), required=True)
    shipping_address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), required=True)
    shipping_depto = forms.CharField(label='Depto', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Depto'}), required=False)
    shipping_city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), required=True)
    shipping_state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), required=False)
    shipping_zip_code = forms.CharField(label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), required=False)
    shipping_country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_address', 'shipping_depto', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_country']
        exclude = ['user']
