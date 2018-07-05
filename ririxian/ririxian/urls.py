
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('df_cart.urls')),
    url(r'^user/', include('df_user.urls')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^order/', include('df_order.urls')),
    url(r'^search/', include('df_goods.urls_search')),
]
