from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']