from django.forms import ModelForm
from django import forms
from pharmacy.models import Pharmacy
from customer.models import customer

class customerForm(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    username =forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    confirm_password= forms.CharField(max_length=20)



