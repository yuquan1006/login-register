from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name","email","createTime")
    list_display_links = ("name",)
    ordering = ("-createTime",)
    # 筛选器
    list_filter = ('name', )  # 过滤器
    search_fields = ('name', )  # 搜索字段
    date_hierarchy = 'createTime'  # 详细时间分层筛选　