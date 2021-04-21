from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    rollnumber = forms.CharField()

    class Meta:
        model = User
        fields = ["username","rollnumber","email","password1","password2"]
        help_texts = {
            'username': None,
            'email': None,
            'rollnumber':None,
            'password1': None,
            'password2': None,
        }