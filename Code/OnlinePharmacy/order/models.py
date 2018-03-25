from django.db import models
#from customer import models as customer_models
#from pharmacy import models as pharmacy_models
from pharmacy.models import Pharmacy
from customer.models import customer
from prescription.models import Prescription
from datetime import datetime
from inventory.models import sells


class order(models.Model):
    pharmacy_id = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    buyer = models.ForeignKey(customer,on_delete=models.CASCADE)#error
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=datetime.now)
    pres_id = models.ForeignKey(Prescription,on_delete=models.CASCADE)
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)
    address_pincode = models.IntegerField()
    delivered_date=models.DateField(blank=True)


class orderOTC(models.Model):
    product_id=models.ForeignKey(sells,on_delete=models.CASCADE)
    buyer = models.ForeignKey(customer,on_delete=models.CASCADE)#error
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=datetime.now)
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)
    address_pincode = models.IntegerField()
    delivered_date=models.DateField(blank=True)