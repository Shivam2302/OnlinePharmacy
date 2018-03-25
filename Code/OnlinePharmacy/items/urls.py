from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

from . import views

app_name='items'
urlpatterns = [
    url(r'^result/$',views.showSearchResult,name="showSearchResult"),
    url(r'^result/(?P<item_id>[0-9]+)/$', views.showSearchResultPharmacy, name="showSearchResultPharmacy"),
    url(r'$', views.showSearch, name="showSearch"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
