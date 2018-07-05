
from django.conf.urls import url,include
from django.contrib import admin
# from  df_goods import  views
from df_goods  import  views_search
urlpatterns = [
    url(r'^$', views_search.index),
]
