from django.conf.urls import url,include
from . import views

app_name='pharmacy'
urlpatterns = [
        url(r'^$',views.showDashboard2,name='showDashboard2'),
        url(r'^notifications/$',views.showNotifications,name="showNotifications"),
        url(r'^notifications/accepted/(?P<prescription_id>[0-9]+)/$',views.acceptNotification,name="acceptNotification"),
        url(r'^detail/(?P<pharmacy_id>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.pharmacy_detail,name="pharmacy_detail"),
        url(r'^p_logout/$',views.p_logout,name="p_logout"),
        url(r'^inventory',include('inventory.urls'))
        ]

