from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    image = models.ImageField()
    otc_or_not = models.BooleanField()
    brand_name = models.CharField(max_length=50)
    salts = models.TextField()
    specifications = models.CharField(max_length=100)
    category = models.CharField(max_length=30)


