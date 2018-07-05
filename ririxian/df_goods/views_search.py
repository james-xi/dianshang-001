# -*- coding: utf-8 -*-
from df_goods.models import GoodsInfo,TypeInfo
from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator

# Create your views here.
# 查询每类商品最新的4个和点击率最高的4个
def index(request):
    """
    根据商品的 信息记性搜索，跳转的页面首先 是根据大类进行 的 区分的更多商品里面，如果是具体的 信息，则 返回具体的 信息
    """
    # 如果 传输的值 是空的话，则默认 的返回首页
    conten = request.GET.get('q')
    if conten:
        pass
    # 进行重定向
    redi = redirect('/goods/')
    return redi





