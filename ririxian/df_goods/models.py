from django.db import models
from  tinymce.models import HTMLField
#  coding: utf-8
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
#商品分类
class TypeInfo(models.Model):
    # title字段的含义是每一类的表题，可以用函数进行表示
    # gtype__id=1    meat 肉类 依次类推 fruit水果  vegetables蔬菜
    #               fish鱼类 egg 鸡蛋  frozen  冷冻食品
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # return self.ttitle.encode('utf-8')
        return self.ttitle
#商品
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    #图片位置    服务器部署记得看看
    # gpic = models.ImageField(upload_to='df_goods')
    gpic = models.ImageField(upload_to='static/img')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    #单位
    gunit = models.CharField(max_length=20,default='500g')
    #点击量  用于排序
    gclick = models.IntegerField()
    #简介
    gjianjie = models.CharField(max_length=200)
    #库存
    gkucun = models.IntegerField()
    #详细介绍
    gcontent = HTMLField()
    #
    gtype = models.ForeignKey(TypeInfo)

    def __str__(self):
        # return self.gtitle.encode('utf-8')
        return self.gtitle
