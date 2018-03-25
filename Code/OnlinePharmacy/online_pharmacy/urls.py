from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from purl.template import patterns

urlpatterns =[
    url(r'',include('Register_and_login.urls')),
    url(r'^homepage/',include('MainPage.urls')),
    url(r'^username/',include('cart.urls')),
    url(r'^username/',include('customer.urls')),
    url(r'^pharmacy_name/',include('pharmacy.urls')),
    url(r'^pharmacy_name/inventory/',include('inventory.urls')),
    url(r'^search/',include('items.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^admin/', admin.site.urls),


]

