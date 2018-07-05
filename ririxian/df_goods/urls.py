
from django.conf.urls import url,include
from django.contrib import admin
# from  df_goods import  views
from df_goods  import  views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^(\d+)/$', views.detail),

]
