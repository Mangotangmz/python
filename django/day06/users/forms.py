
from django import forms


class UserForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True,max_length=10)
    icon = forms.ImageField(required=True)