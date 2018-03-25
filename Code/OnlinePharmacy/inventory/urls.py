from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'show/',views.showInventory,name="showInventory"),
    url(r'^/create/$', views.addItemInInventory, name="addItemInInventory"),
    url(r'^/create/(?P<item_id>[0-9]+)/$', views.createInventory1,name="createInventory1"),
    url(r'^/create/items/$', views.addItemInInventoryResult, name="addItemInInventoryResult"),
    url(r'^/addNew/$',views.addNewProduct,name="addNewProduct")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
