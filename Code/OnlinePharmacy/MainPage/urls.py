from django.conf.urls import url,include
from . import views

app_name='MainPage'
urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    url(r'^welcome/$',views.userPage,name="userPage")
    ]