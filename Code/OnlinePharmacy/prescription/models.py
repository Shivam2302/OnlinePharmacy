from django.db import models
from customer.models import customer
from pharmacy.models import Pharmacy


# Create your models here.
class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    prescription_image = models.ImageField()
    uploaded_by = models.ForeignKey(customer)
    flag_for_fulfillment = models.BooleanField(default=False)


