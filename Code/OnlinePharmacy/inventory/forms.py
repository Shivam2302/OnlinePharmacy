from django import forms

from django.forms import ModelForm

from django.apps import apps
# from inventory.models import sells
from items.models import Item
from inventory.models import sells

class InventoryForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_id','item_name','image','otc_or_not','salts','brand_name','specifications','category']






class SellsForm(ModelForm):
    class Meta:
        model = sells
        fields = ['quantity', 'price_per_item']

