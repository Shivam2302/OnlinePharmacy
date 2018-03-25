from django.conf.urls import url,include
from . import views
app_name = 'customer'
urlpatterns = [
    url(r'^$', views.showHomepage1, name='showHomepage1'),
   url(r'^dashboard/$',views.showDashboard1,name="showDashboard1"),
    url(r'^dropdown/$',views.dropdown,name="dropdown"),
    url(r'^dashboard/addresslog/$',views.address_log,name="address_log"),
    url(r'^dashboard/orderlog/$',views.order_log,name="order_log"),
    url(r'^dashboard/notifications/$',views.showNotifications,name="showNotifications"),
    url(r'^saveChanges/$',views.saveChanges,name="saveChanges"),
    url(r'^deleteAddress/(?P<id>[0-9]+)$',views.deleteAddress,name="deleteAddress"),
    url(r'^addnewAddress/',views.user_contact,name="addnewAddress"),
    url(r'^logout/$',views.logout,name="logout"),

    ]


