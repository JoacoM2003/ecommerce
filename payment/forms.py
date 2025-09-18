from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), required=False)
    shipping_email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), required=False)
    shipping_address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), required=False)
    shipping_depto = forms.CharField(label='Depto', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Depto'}), required=False)
    shipping_city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), required=False)
    shipping_state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), required=False)
    shipping_zip_code = forms.CharField(label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), required=False)
    shipping_country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email','shipping_address', 'shipping_depto', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_country']
        exclude = ['user']

class PaymentForm(forms.Form):
    card_name = forms.CharField(label='Card Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Name'}), required=False)
    card_number = forms.CharField(label='Card Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'}), required=False)
    card_exp_date = forms.CharField(label='Card Exp Date', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Exp Date'}), required=False)
    card_cvv = forms.CharField(label='Card CVV', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card CVV'}), required=False)
    card_address = forms.CharField(label='Card Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Address'}), required=False)
    card_depto = forms.CharField(label='Card Depto', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Depto'}), required=False)
    card_city = forms.CharField(label='Card City', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card City'}), required=False)
    card_state = forms.CharField(label='Card State', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card State'}), required=False)
    card_zip_code = forms.CharField(label='Card Zip Code', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Zip Code'}), required=False)
    card_country = forms.CharField(label='Card Country', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Country'}), required=False)
    