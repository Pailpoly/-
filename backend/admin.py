from django.contrib import admin

# Register your models here.
from django.contrib import admin
from backend.models import *  # 导入模型类



admin.site.site_header = "后台管理系统"
admin.site.site_title = "欢迎进入后台管理~"
admin.site.index_title = "我的项目"

admin.site.register(yyyyy)
admin.site.register(myusertwommmm)#用户扩展表

admin.site.register(GCategorymmmm)# 注册city表
admin.site.register(GProductmmmm)  # 注册book表
admin.site.register(ddaddress)  # 注册book表
admin.site.register(wxdindan)  # 注册book表


