from django.contrib import admin

# Register your models here.
from items.models import Item

admin.site.register(Item)