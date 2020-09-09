from django.db import models

# Create your models here.


from django.db import models


class yyyyy(models.Model):
    name=models.CharField('商品名',null=True,blank=True,max_length=300)
    small_image=models.ImageField(upload_to='drug_img/%Y/%m/%d/', verbose_name='商品图片')


############################################################用户表

from django.db import models

# Create your models here.

#django怎么设计数据表
#django信号详解

#系统User表  用户名用openid  密码也用它  邮箱设默认xyz@qq.com
from django.contrib.auth.models import  User
from django.dispatch import receiver
from django.db.models.signals import  post_save#django信号道,相当于js中的事件
from datetime import datetime

class myusertwommmm(models.Model):
    user_type_choics = (
        (1, "普通用户"),
        (2, "普通会员"),
        (3, "白金会员"),
        (4, "黄金会员"),
    )
    user = models.OneToOneField( User, related_name="extension", on_delete= models.CASCADE )#关联User表
    openid=models.CharField('微信openid',max_length=500,null=True,blank=True)#存openid
    nickname=models.CharField('微信名',max_length=200,null=True,blank=True)#存微信名
    gender=models.CharField('性别',max_length=2,null=True,blank=True)#存性别 1为男 0为女
    city=models.CharField('城市',max_length=200,null=True,blank=True)#城市
    province=models.CharField('省',max_length=200,null=True,blank=True)#省
    contry=models.CharField('国家',max_length=200,null=True,blank=True)#国家
    avatarurl=models.CharField('微信头像URL',max_length=2000,null=True,blank=True)#微信头像


    phone = models.CharField('手机号',max_length=11,null=True,blank=True)#存手机号
    #icon_image=models.ImageField('头像',upload_to='icon_img/%Y/%m/%d/',null=True,blank=True)
    #l_edit = models.DateTimeField('编辑时间', auto_now_add=True,null=True,blank=True)
    c_time = models.DateTimeField('添加时间', auto_now=True,null=True,blank=True)
    user_type = models.IntegerField('用户等级',choices=user_type_choics,null=True,blank=True)
    token=models.CharField(max_length=3000,null=True,blank=True)
    expiration_time = models.DateTimeField(default=datetime.now, verbose_name="过期时间",null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="token添加时间",null=True,blank=True)
    class Meta:
        ordering=['id']
        verbose_name = '用户扩展表'
        verbose_name_plural = '用户扩展表'



@receiver(post_save, sender = User)
def create_user_extension( sender, instance, created, **kwargs ):
    if created:
        myusertwommmm.objects.create( user = instance)
    else:
        instance.extension.save()




#########################################################分类表

class GCategorymmmm(models.Model):
    title=models.CharField(null=True,blank=True,max_length=300)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['id']
        verbose_name = '分类表'
        verbose_name_plural = '分类表'


##########################################################################商品表


from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField#头部增加这行代码导入import datetime


class GProductmmmm(models.Model):
    name=models.CharField('商品名',null=True,blank=True,max_length=300)
    small_image=models.ImageField(upload_to='drug_img/%Y/%m/%d/', verbose_name='商品图片')
    price=models.IntegerField('现价',null=True,blank=True,default=89) #现价
    origin_price=models.IntegerField('原价',null=True,blank=True,default=99)#原价
    spec=models.TextField('简述',null=True,blank=True,default="None")#描述
    total_sales=models.IntegerField('销量',null=True,blank=True,default=0) #总销量
    vip_price=models.IntegerField('会员价',null=True,blank=True,default=79) #会员
    category=models.ForeignKey(verbose_name='分类',to=GCategorymmmm,on_delete=models.DO_NOTHING)
    body = UEditorField('商品详细说明', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    # def __str__(self):
    #     return self.name
    class Meta:
        ordering=['id']
        verbose_name = '商品表'
        verbose_name_plural = '商品表'



################################################################地址表-----我们关联myusertwommmm表

class ddaddress(models.Model):

    # (1, "默认地址"),
    # (2, "普通地址")
    auser = models.CharField('用户id', max_length=5)  #  # 关联User表多对一
    aname = models.CharField('收货人', max_length=60, null=True, blank=True)  #
    aphone = models.CharField('手机号', max_length=20, null=True, blank=True)  #
    city = models.CharField('省市', max_length=500, null=True, blank=True)  #
    aaddress = models.CharField('详细地址', max_length=500, null=True, blank=True)  #
    adefaultaddress = models.CharField('是否默认地址', max_length=5,default="2")  #


    class Meta:
        ordering = ['id']
        verbose_name = '地址表'
        verbose_name_plural = '地址表'



##################################################################订单表

class wxdindan(models.Model):
    #pass
    #关联:与用户表多对一,与地址表一对一,商品表没有设关联,
    #1为微信支付,   2为支付宝支付,,,还可以扩展更多方式
    #注,优化时,可以除掉有些重复的字段,比如wxopenid,放在这只是为了快速方便开发,不要让表关联太深,这样查询时,会拖慢后端,先设计如此,后期还会改
    wxuserid= models.ForeignKey(myusertwommmm, related_name="wxdindanextension", on_delete= models.CASCADE,verbose_name=u'用户' )#关联myusertwo表多对一
    wxopenid=models.CharField('用户openid',max_length=1000,null=True,blank=True)
    wxusertext=models.CharField('用户留言',max_length=1000,null=True,blank=True)
    fapiao=models.CharField('发票抬头',max_length=1000,null=True,blank=True)#发票可以单独分离出一张表更好
    fapiaohaoma=models.CharField('发票税号',max_length=1000,null=True,blank=True)#发票可以单独分离出一张表更好
    paymode=models.CharField('支付方式',max_length=1000,null=True,blank=True,default="1")#发票可以单独分离出一张表更好
    #addressid= models.OneToOneField('ddaddress',on_delete=models.CASCADE,related_name='dindanaddressextension')   #OneToOneField 是一对一地址表
    addressid = models.CharField('地址ID', max_length=1000, null=True, blank=True)  #

    productid=models.CharField("商品id",max_length=1000,null=True,blank=True)
    count=models.CharField('购买数量',max_length=1000,null=True,blank=True)#单款商品的数量
    payzt=models.CharField('支付状态',max_length=1000,null=True,blank=True)#等待支付,或支付成功等等
    dindanbianhao = models.CharField('订单编号', max_length=200, null=True, blank=True)
    totalprice=models.CharField('总货款', max_length=200, null=True, blank=True)#单款商品的总价款
    add_time = models.DateTimeField(default=datetime.now, verbose_name="提交订单时间", null=True, blank=True)

    # def __str__(self):#不设它,不想只返回一个字段
    #     return self.xyzdindanbianhao
    class Meta:
        ordering=['id']
        verbose_name = '订单表'
        verbose_name_plural = '订单表'




















