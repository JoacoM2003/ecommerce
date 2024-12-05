from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

# class UserInfoForm(forms.ModelForm):
#     phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}), required=False)
#     address1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), required=False)
#     address2 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), required=False)
#     city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), required=False)
#     state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), required=False)
#     zip_code = forms.CharField(label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), required=False)
#     country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), required=False)

#     class Meta:
#         model = Profile
#         profiles = ['phone', 'address1', 'address2', 'city', 'state', 'zip_code', 'country']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = 'Required. 8 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password (again)'
        self.fields['password2'].label = 'Password (again)'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email ya existe')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = 'Password'
        self.fields['password'].help_text = 'Required. 8 characters or fewer. Letters, digits and @/./+/-/_ only.'

class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = 'Email'
        self.fields['email'].help_text = 'Required. Enter a valid email address.'

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Email ya existe')
        return data
    

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = 'Password'
        self.fields['new_password1'].help_text = 'Required. 8 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Password (again)'
        self.fields['new_password2'].label = 'Password (again)'
        self.fields['new_password2'].help_text = 'Enter the same password as before, for verification.'