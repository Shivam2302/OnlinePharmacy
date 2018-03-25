from django.db import models
from django.apps import apps
from customer.models import customer
from items.models import Item
from inventory.models import sells

class contains(models.Model):
    cart_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(sells,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ['cart_id', 'product_id']
