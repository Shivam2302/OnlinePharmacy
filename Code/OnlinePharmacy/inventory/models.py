from django.db import models
#from pharmacy import models as pharmacy_models
#from items import models as item_models
from items.models import Item
from pharmacy.models import Pharmacy

class sells(models.Model):
    #pharmacy_id = models.OneToOneField(pharmacy, primary_key=True)
    pharmacy_id = models.ForeignKey(Pharmacy,on_delete = models.CASCADE)
    #item_id = models.OneToOneField(Item)
    item_id = models.ForeignKey(Item,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price_per_item = models.FloatField()

    class Meta:
        unique_together = ('pharmacy_id', 'item_id')

