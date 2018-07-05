from django.contrib import admin

# Register your models here.
# from  ririxian.df_goods.models import TypeInfo,GoodsInfo
from df_goods.models import GoodsInfo,TypeInfo
@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ["gtitle", "gpic", "gprice", "isDelete", "gunit", "gclick", "gjianjie","gkucun","gcontent","gtype"]
    list_filter = ["gtype","isDelete" ,"gunit", "gclick","gkucun"]
    search_fields = ["gtitle"]
    list_per_page = 10
    # 执行动作框的位置
    actions_on_top = False
    actions_on_bottom = True

    #添加、修改页属性
    fieldsets = [
        ("base", {"fields":["gtitle","gpic","gprice","gjianjie","gcontent"]}),
        ("more", {"fields": ["gtype", "isDelete"]}),
    ]
# admin.site.register(Student, StudentAdmin)


class GoodsInfoInLine(admin.TabularInline):
    model = GoodsInfo
    extra = 2
@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    inlines = [GoodsInfoInLine]
    list_display = ["ttitle", "isDelete"]
    list_filter = ["ttitle"]
    search_fields = ["ttitle"]
    list_per_page = 10
    fields = ["ttitle", "isDelete"]
