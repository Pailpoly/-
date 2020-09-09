"""mydangdang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend.views import *
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('useralldindan/',useralldindan),#用户id取出该用户所有订单
    path('payOrder/',payOrder),#支付接口
    path('gotodindan/',gotodindan),#支付成功后的数据写入数据库
    path('addressgotomypay/',addressgotomypay),#改为默认地址
    path('Changeaddress/',Changeaddress),#修改地址
    path('addaddress/',addaddress),#新建地址,参数有1个,用户id,地址
    path('deladdress/',deladdress),#按指定id删除地址
    path('getalladdress/',getalladdress),#用户id取出该用户所有关联的地址
    path('mycardata/',mycardata),#购物车页面取商品数据
    path('test/', test),
    path('mypro/',mypro),#接收前端商品ID,获取该商品对象给前端,商品详情页
    path('vvv/',vvv),#分类表和商品的总合接口
    path('usertest/',usertest),#测试用户扩展表
    path(r'ueditor/', include('DjangoUeditor.urls'))
    #path('test2/', test2),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
