from django.forms import ModelForm
from django import forms
from pharmacy.models import Pharmacy
from customer.models import customer
from pharmacy.models import STATES



class PharmacyRegistration(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Pharmacy
        fields = ['pharmacy_id','pharmacy_name','owner_fname','owner_lname','vat_no',
                  'drug_license','address_street','address_city','address_state',
                  'address_pincode','password']
        widgets = {
            'password': forms.PasswordInput(),
        }


    def clean_address_pincode(self):
        pincode = self.cleaned_data['address_pincode']
        if(pincode <=100000 or pincode>=999999):
                raise forms.ValidationError("Invalid Pincode")
        return pincode


    def clean(self):
        cleaned_data = super(PharmacyRegistration, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )




class CustomerRegistration(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = customer
        fields = ['username','fname','lname','age',
                  'email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }


    def clean_email(self):
        if customer.objects.filter(email=self.cleaned_data.get('email',None)).count()>0:
            raise forms.ValidationError("Email already exists")
        return self.cleaned_data.get('email')


    def clean_age(self):
        age = self.cleaned_data['age']
        if age <=0:
            raise forms.ValidationError("Invalid Age")
        return age


    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data["password"]
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")





class CustomerLogin(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter your username or email'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))




class PharmacyLogin(forms.Form):
    pharmacy_id = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password '}))

class PharmacyContact(forms.Form):
    contact_no = forms.IntegerField()
    alternate_no = forms.IntegerField()

    def clean_contact_no(self):
        number = self.cleaned_data['contact_no']
        if  number<1000000000 or number>9999999999:
            raise forms.ValidationError("Invalid Mobile Number")
        return number

    def clean_alternate_no(self):
        number = self.cleaned_data['alternate_no']
        if  number<1000000000 or number>9999999999:
            raise forms.ValidationError("Invalid Mobile Number")
        return number





class UserContact(forms.Form):
    contact_no = forms.IntegerField()
    alternate_no = forms.IntegerField()
    address_street = forms.CharField(max_length=200)
    address_city = forms.CharField(max_length=20)
    address_state = forms.CharField(max_length=20,widget=forms.Select(choices=STATES))
    address_pincode = forms.IntegerField()

    def clean_contact_no(self):
        number = self.cleaned_data['contact_no']
        if number <= 6000000000 or number >= 9999999999:
            raise forms.ValidationError("Invalid Mobile Number")
        return number

    def clean_alternate_no(self):
        number = self.cleaned_data['alternate_no']
        if number <= 6000000000 or number >= 9999999999:
            raise forms.ValidationError("Invalid Mobile Number")
        return number

    def clean_address_pincode(self):
        pincode = self.cleaned_data['address_pincode']
        if(pincode <=100000 or pincode>=999999):
                raise forms.ValidationError("Invalid Pincode")
        return pincode


