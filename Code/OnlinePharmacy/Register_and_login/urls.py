from django.conf.urls import url
from . import views
app_name='Register_and_login'
urlpatterns = [
    url(r'^user/registration/', views.user_registration, name='user_registration'),
    url(r'^user/contact/', views.user_contact, name='user_contact'),
    url(r'^user/login', views.user_login, name='user_login'),
    url(r'^pharmacy/registration', views.pharmacy_registration, name='pharmacy_registration'),
    url(r'^pharmacy/contact', views.pharmacy_contact, name='pharmacy_contact'),
    url(r'^pharmacy/login', views.pharmacy_login, name='pharmacy_login'),

    url(r'^$', views.index, name='index')
]



