from django import forms

from django.forms import ModelForm

from prescription.models import Prescription


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['prescription_image',]
