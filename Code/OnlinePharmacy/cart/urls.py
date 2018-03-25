from django.conf.urls import url,include
from . import views

app_name='cart'
urlpatterns = [
    url(r'^cart/$',views.showCart,name='showCart'),
    url(r'^addToCart/(?P<item_id>[0-9]+)/$',views.addItem,name='addItem'),
    url(r'^addToCart/(?P<pharmacy_id>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<item_id>[0-9]+)/$', views.addItemByParticularPharmacy, name='addItemByParticularPharmacy('),
    url(r'^deletefromcart/(?P<item_id>[0-9]+)/(?P<pharmacy_id>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deleteItem,name='deleteItem'),
    url(r'^emptycart/$',views.emptyCart,name='emptyCart'),
    url(r'^updateCart/(?P<id>[0-9]+)/$',views.updateCart,name="updateCart"),
    url(r'^itemCheckout/(?P<id>[0-9]+)/$', views.itemCheckout, name="itemCheckout,"),
    ]
