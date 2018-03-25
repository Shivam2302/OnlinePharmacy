from django.db import models
from customer.models import customer
from pharmacy.models import Pharmacy
from prescription.models import Prescription


class notifications_to_pharmacy(models.Model):
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    time_of_arrival = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()
    sent_by_customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    prescription_image = models.ImageField(blank=True)
    prescription_id = models.ForeignKey(Prescription,on_delete=models.CASCADE)


class Notifications_to_user(models.Model):
    username_reciever = models.ForeignKey(customer, on_delete=models.CASCADE)
    time_of_arrival = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()
    sent_by_pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)


