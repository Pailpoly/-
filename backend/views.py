from urllib.parse import parse_qs

import demjson
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse


def test(request):
    return JsonResponse({"status":0,"message":"这是django后台数据"},safe=False,json_dumps_params={'ensure_ascii':False})


####################################用户登陆成功,信息写入用户表,并把id传入前端
import json
from backend.models import *
def usertest(request):
    if request.method == "POST":
        print(request.body)

        body_unicode = request.body.decode('utf-8')
        body = demjson.encode(body_unicode)
        body = json.loads(body)
        # body=demjson.decode((body))
        print("我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
        print(type(body))  # <class 'str'>

        params = parse_qs(body)
        print(type(body))  # <class 'str'>
        data = json.loads(body)
        print("data", data)
        print("data类型", type(data))  # dict字典,json对象
        print("接收前端的openid", data["myopenid"])
        print("接收前端的用户详细信息", data['myuserinfo'])

        openid = data["myopenid"]  # 取用户微信openid
        userinfo = data['myuserinfo']  # 取用户其它信息
        # 处理性别,先不处理,让前端处理,因为从腾迅回调拿 到的本来就是1...或  0

        #在写入前加个判断,数据库中是否已有该openid的用户
        myppp=myusertwommmm.objects.filter(openid=openid)#如有,则不是空数组,如无,则为空数组
        if myppp:#如果不为空,已有该用户
            #return HttpResponse(myppp.id)
            print(myppp[0].id)
            return HttpResponse(myppp[0].id)
        else:#如果不存在此用户
            user = User.objects.create_user(username=openid, password=openid, email="xyz@qq.com")  # 存入系统User表
            user.extension.openid = openid  # 下面都是myusertwo的写入
            user.extension.nickname = userinfo['nickName']
            user.extension.city = userinfo['city']
            user.extension.province = userinfo['province']
            user.extension.contry = userinfo['country']  # 注意,单词,两个不一样,我的少写了一个n
            user.extension.avatarurl = userinfo['avatarUrl']  # 单词注意,大小写
            user.extension.gender = userinfo['gender']
            user.save()
            # 来个保险,取出myusertwo表中,该用户的id,传到前端,User已存在,前端暂时用不着,先不管
            usertwo = myusertwommmm.objects.filter(openid=data["myopenid"])  # 结果为对象数组,里面只有一个对象
            getid = usertwo[0].id

            #return HttpResponse(getid)
            return HttpResponse(getid)
    else:
        return HttpResponse("这是一个GET请求")






















######################################################################如下是分类表和商品表的总合接口

from django.http import HttpResponse, JsonResponse  # , JsonResponse

from django.shortcuts import render, HttpResponse
from django.db import  connection
from django.contrib.auth.models import  User
from urllib.parse import parse_qs, urlparse
import demjson
import json
#pip install demjson
import ast
from rest_framework import serializers


#做商品分类和商品的接口以及转为前端所需格式

#自定义  分类和商品数据

class xiupro(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = GProductmmmm  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        #depth = 1  # 深度为1

def dddpro():
    shopcart_list = GProductmmmm.objects.all()
    serializer=xiupro(shopcart_list,many=True)#序列化
    return serializer.data  # 把数据传出去

class xiucate(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = GCategorymmmm  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        #depth = 1  # 深度为1

def dddcate():
    shopcart_list =GCategorymmmm.objects.all()
    serializer=xiucate(shopcart_list,many=True)#序列化
    return serializer.data  # 把数据传出去





def vvv(request):
    #先做一下空架子
    mydata={}
    # mydata["code"]=200
    # mydata["message"]="success"
    mydata["data"]=[]

    #做2序列化器,分别得到json数据

    ccc = {}
    ppp={}

    ccc = dddcate()  # 取上面函数传出来的数据,是字典
    ppp=dddpro()
    print("ccc",ccc)
    print("ppp",ppp)
    kkk = json.dumps(ccc)  # 把数据字典转为JSON对象格式,前端才可以用
    mmm=json.dumps(ppp)
    print(kkk)#拿到分类
    print(mmm)#拿到商品
    mydata["data"]=ccc
    #如上,外层已做好,下面,只用将各个分类的商品取出放在外层的分类中

    #下面 i 为数组内的每一项,t为循环下标,以0开始
    for t,i in enumerate(mydata["data"]):
        #print(i)#OrderedDict
        print(i["id"])#拿到所有id值
        print("t",t)#输出的是循环下标0开始
        mydata["data"][t]["product"]=[]
        # print(mydata["goods"][i]["foods"])
        for o in ppp:
            #print(o['category'])#拿到商品中的各种分类
            if o['category']==i["id"]:
                mydata["data"][t]["product"].append(o)

                #print(list(o))#将字典dick转为list数组
                #mylist=list(o)
                #mydata["goods"][i]["foods"].append(mylist)
                #print(mylist)


    return JsonResponse(mydata, safe=False,json_dumps_params={'ensure_ascii':False})




###############################################################################商品详情页取商品对象用ID

#据ID,获得对应商品
class xiuprommmm(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = GProductmmmm  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        depth = 1  # 深度为1


def mypro(request):
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("xxx我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
    proid=json.loads(body)
    myid=proid['id']#取出了商品id值
    print("前端传来的ID:",myid)

    shopcart_list = GProductmmmm.objects.filter(id=myid)  # 筛选再传到前端
    serializer = xiuprommmm(shopcart_list, many=True)
    # 把数据库数据调出来并序列化,成json传到前端
    ttt = {}
    # myjson = djangojson()# 取QuerySet为json
    # #objStr = json.loads(myjson)#转为字符串
    # kkk=json.dumps(myjson)#处理之后前端才能接收 ,kkk此时为字符串,不是列表,也不是字典,是纯的字符串
    jjj = serializer.data  # 取上面函数传出来的数据,是字典
    print(jjj)
    print("#" * 20)
    print(json.dumps(jjj))
    kkk = json.dumps(jjj)  # 把数据字典转为JSON对象格式,前端才可以用
    ttt["kkk"] = kkk
    # return render(request,"course_shopcart.html",ttt)  ##这个是主函数,这个会往页面中增加数据
    return HttpResponse(kkk)  # 这个会直接覆盖网页中所有的数据


################################################################################################
###################################################################################################取购物车商品
class asdfjkkkl(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = GProductmmmm  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        # depth = 1  # 深度为1


def mycardata(request):
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("xxx我将参数转为字符串" + body)
    # xxx我将参数转为字符串{"cardata":[{"id":"6","num":33},{"id":"9","num":3},{"id":"11","num":2}]}
    proid = json.loads(body)
    print("打印一下类型", type(proid))  # 打印一下类型 <class 'dict'>
    print(proid)
    mmm = proid['cardata']
    print('mmm', mmm)  # [{'id': '6', 'num': 33}, {'id': '9', 'num': 3}, {'id': '11', 'num': 2}]  对象数组
    zzz = []

    for i in mmm:
        pid = i['id']
        # pnum=i['num']
        # print(pid)#打印出所有ID
        plist = GProductmmmm.objects.get(id=pid)  # 用id查出商品,结果为商品对象数组,不能用get,只返回商品名
        zzz.append(plist)

    print("zzz", zzz)  # 商品表之对象数组
    print(type(zzz))

    serializer = asdfjkkkl(zzz, many=True)
    jjj = serializer.data
    kkk = json.dumps(jjj).encode('utf-8').decode('unicode_escape')  # 把数据字典转为JSON对象格式,前端才可以用
    ##此时kkk为json对象,在前端就是对象数组   mmm也是对象数组

    return HttpResponse(kkk)  # 这个会直接覆盖网页中所有的数据





############################################################################用户id取出该用户所有关联的地址
#getalladdress
class xiuproxxx(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        # model=ShopCart#获取所有购物车表中的数据，并序列化
        model = ddaddress  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        #depth = 1  # 深度为1


def getalladdress(request):
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
    print(type(body))  # <class 'str'>

    params = parse_qs(body)
    print(type(body))  # <class 'str'>
    data = json.loads(body)
    print("data", data)
    print("data类型", type(data))  # dict字典,json对象
    print("接收前端的id", data["myid"])
    myid=data["myid"]#myid就是前端传过来的用户id了. ,


    shopcart_list = ddaddress.objects.filter(auser=myid)  # 筛选再传到前端
    serializer = xiuproxxx(shopcart_list, many=True)
    # 把数据库数据调出来并序列化,成json传到前端
    ttt = {}
    # myjson = djangojson()# 取QuerySet为json
    # #objStr = json.loads(myjson)#转为字符串
    # kkk=json.dumps(myjson)#处理之后前端才能接收 ,kkk此时为字符串,不是列表,也不是字典,是纯的字符串
    jjj = serializer.data  # 取上面函数传出来的数据,是字典
    print(jjj)
    print("#" * 20)
    print(json.dumps(jjj))
    kkk = json.dumps(jjj)  # 把数据字典转为JSON对象格式,前端才可以用
    ttt["kkk"] = kkk
    # return render(request,"course_shopcart.html",ttt)  ##这个是主函数,这个会往页面中增加数据
    return HttpResponse(kkk)  # 这个会直接覆盖网页中所有的数据




######################################################################指定id删除地址

#删除地址
def deladdress(request):
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
    print(type(body))  # <class 'str'>

    params = parse_qs(body)
    print(type(body))  # <class 'str'>
    data = json.loads(body)
    print("data", data)
    print("data类型", type(data))  # dict字典,json对象
    print("接收前端的id", data["addressid"])
    myid = data["addressid"]  # myid就是前端传过来的用户id了 ,
    #上面代码,完美收到参数
    ddaddress.objects.filter(id=myid).delete()

    return HttpResponse("后端已完成地址删除")


######################################################################################新增地址

#新增地址
def addaddress(request):
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
    print(type(body))  # <class 'str'>

    params = parse_qs(body)
    print(type(body))  # <class 'str'>
    data = json.loads(body)
    print("data", data)
    print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象", data["addobj"])#{'username': '2323', 'telphone': '212', 'address': '1231', 'default': 1, 'userid': 30}
    myobj = data["addobj"]  # {'username': '2323', 'telphone': '212', 'address': '1231', 'default': 1, 'userid': 30}
    # 上面代码,完美收到参数
    userid=myobj['userid']
    myname=myobj['username']
    mcity=myobj['city']

    myphone=myobj['telphone']
    myaddress=myobj['address']
    myadefaultaddress=myobj['default']
    print(userid,myname,myphone,myaddress,myadefaultaddress)#测试,完美取到




    #操作默认地址
    if myobj['default']==1:#如果添加的地址设了默认地址,则要把之前的默认地址改为普通地址
        obja = ddaddress.objects.get(adefaultaddress=1)
        obja.adefaultaddress = 2
        obja.save()

    #先取myusertwo表对象
    #mypk=User.objects.get(id=userid)
    #写入数据库
    ddaddress.objects.create(auser=userid,aname=myname,aphone=myphone,aaddress=myaddress,adefaultaddress=myadefaultaddress,city=mcity)
    #如上,成功写入地址表,但有一个问题,默认地址只能有一个,所以,在写入之前,要判断
    return HttpResponse("地址已存入数据库")


########################################################################################修改地址

#修改地址Changeaddress
def Changeaddress(request):
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)
    # body=demjson.decode((body))
    print("我将参数转为字符串" + body)  # username=15323441764&addressid=15&productid=19&pnum=4&myprice=356
    print(type(body))  # <class 'str'>

    params = parse_qs(body)
    print(type(body))  # <class 'str'>
    data = json.loads(body)
    print("data", data)
    print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象",data["addobj"])  # {'username': '2323', 'telphone': '212', 'address': '1231', 'default': 1, 'userid': 30}
    myobj = data["addobj"]  # {'username': '2323', 'telphone': '212', 'address': '1231', 'default': 1, 'userid': 30}
    # 上面代码,完美收到参数



    aid = myobj['aid']
    myname = myobj['username']
    mcity = myobj['city']
    myphone = myobj['telphone']
    myaddress = myobj['address']
    myadefaultaddress = myobj['default']
    print(aid, myname, myphone, myaddress, myadefaultaddress, mcity)  # 测试,完美取到



    # 操作默认地址
    if myobj['default'] == 1:  # 如果添加的地址设了默认地址,则要把之前的默认地址改为普通地址
        # 先取出所有地址
        ttt = ddaddress.objects.filter(adefaultaddress=1)
        print(len(ttt))  # 0无默认地址时
        if len(ttt) > 0:  # 有默认地址才操作
            obja = ddaddress.objects.get(adefaultaddress=1)
            print("obja", obja)  # 为[],如无默认地址
            obja.adefaultaddress = 2
            obja.save()

    ddaddress.objects.filter(id=aid).update(aname=myname,aphone=myphone,city=mcity,aaddress=myaddress,adefaultaddress=myadefaultaddress)

    return HttpResponse("地址已修改完成")




###############################################################设为默认地址
#点击地址列表页list.vue的地址,就改为默认地址,
def addressgotomypay(request):
    #print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)


    params = parse_qs(body)
    #print(type(body))  # <class 'str'>
    data = json.loads(body)
    #print("data", data)
    #print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象-许",data["myid"])  # {'username': '2323', 'telphone': '212', 'address': '1231', 'default': 1, 'userid': 30}
    myid = data["myid"]  # 取到地址id

    ttt = ddaddress.objects.filter(adefaultaddress=1)
    print(len(ttt))  # 0无默认地址时
    if len(ttt) > 0:  # 有默认地址才操作
        obja = ddaddress.objects.get(adefaultaddress=1)
        obja.adefaultaddress = 2
        obja.save()

    ddaddress.objects.filter(id=myid).update(adefaultaddress=1)

    return HttpResponse("已改为默认地址")

##################################################################################################下面是支付
##################################################################################################################支付测试
##################################################################################################################支付测试
# 微信支付的配置参数
# client_appid = ''  # 小程序appid
# client_secret = ''  # 小程序secret
#
# Mch_id = ''  # 商户号,之前无意后面多了个空格,提示mch_id参数出错
# Mch_key = ''  # 商户Key
client_appid = 'wx8f60753d3939d7c1'  # 小程序appid
client_secret = '3a6d2dbc28ab675806c1a7691e0ae46a'


Mch_id = '1579508001'  # 商户号,之前无意后面多了个空格,提示mch_id参数出错
Mch_key = '75ce7b9b947aff0b86398281656774a2'  # 商户Key
order_url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'  # 订单地址
import hashlib
import datetime
import xml.etree.ElementTree as ET
import requests
#from ..models import users

# 生成签名的函数
def paysign(appid, body, mch_id, nonce_str, notify_url, openid, out_trade_no, spbill_create_ip, total_fee):
    ret = {
        "appid": appid,
        "body": body,
        "mch_id": mch_id,
        "nonce_str": nonce_str,
        "notify_url": notify_url,
        "openid": openid,
        "out_trade_no": out_trade_no,
        "spbill_create_ip": spbill_create_ip,
        "total_fee": total_fee,
        "trade_type": 'JSAPI'
    }
    print(ret)
    # 处理函数，对参数按照key=value的格式，并按照参数名ASCII字典序排序
    stringA = '&'.join(["{0}={1}".format(k, ret.get(k)) for k in sorted(ret)])
    stringSignTemp = '{0}&key={1}'.format(stringA, Mch_key)
    sign = hashlib.md5(stringSignTemp.encode("utf-8")).hexdigest()
    print(sign.upper())
    return sign.upper()


# 生成随机字符串
def getNonceStr():
    import random
    data = "123456789zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP"
    nonce_str = ''.join(random.sample(data, 30))
    return nonce_str


# 生成商品订单号
def getWxPayOrdrID():
    date = datetime.datetime.now()
    # 根据当前系统时间来生成商品订单号。时间精确到微秒
    payOrdrID = date.strftime("%Y%m%d%H%M%S%f")
    print("支付时生成的订单编号",payOrdrID)
    return payOrdrID


# 获取全部参数信息，封装成xml
def get_bodyData(openid, client_ip, price):
    body = 'Mytest'  # 商品描述
    notify_url = 'https://127.0.0.1:80/payOrder/'  # 支付成功的回调地址  可访问 不带参数
    nonce_str = getNonceStr()  # 随机字符串
    out_trade_no = getWxPayOrdrID()  # 商户订单号
    total_fee = str(price)  # 订单价格 单位是 分

    # 获取签名
    sign = paysign(client_appid, body, Mch_id, nonce_str, notify_url, openid, out_trade_no, client_ip, total_fee)

    bodyData = '<xml>'
    bodyData += '<appid>' + client_appid + '</appid>'  # 小程序ID
    bodyData += '<body>' + body + '</body>'  # 商品描述
    bodyData += '<mch_id>' + Mch_id + '</mch_id>'  # 商户号
    bodyData += '<nonce_str>' + nonce_str + '</nonce_str>'  # 随机字符串
    bodyData += '<notify_url>' + notify_url + '</notify_url>'  # 支付成功的回调地址
    bodyData += '<openid>' + openid + '</openid>'  # 用户标识
    bodyData += '<out_trade_no>' + out_trade_no + '</out_trade_no>'  # 商户订单号
    bodyData += '<spbill_create_ip>' + client_ip + '</spbill_create_ip>'  # 客户端终端IP
    bodyData += '<total_fee>' + total_fee + '</total_fee>'  # 总金额 单位为分
    bodyData += '<trade_type>JSAPI</trade_type>'  # 交易类型 小程序取值如下：JSAPI
    bodyData += '<sign>' + sign + '</sign>'
    bodyData += '</xml>'

    return bodyData


def xml_to_dict(xml_data):
    '''
    xml to dict
    :param xml_data:
    :return:
    '''
    xml_dict = {}
    root = ET.fromstring(xml_data)
    for child in root:
        xml_dict[child.tag] = child.text
    return xml_dict


def dict_to_xml(dict_data):
    '''
    dict to xml
    :param dict_data:
    :return:
    '''
    xml = ["<xml>"]
    for k, v in dict_data.iteritems():
        xml.append("<{0}>{1}</{0}>".format(k, v))
    xml.append("</xml>")
    return "".join(xml)


# 获取返回给小程序的paySign
def get_paysign(prepay_id, timeStamp, nonceStr):
    pay_data = {
        'appId': client_appid,
        'nonceStr': nonceStr,
        'package': "prepay_id=" + prepay_id,
        'signType': 'MD5',
        'timeStamp': timeStamp
    }
    stringA = '&'.join(["{0}={1}".format(k, pay_data.get(k)) for k in sorted(pay_data)])
    stringSignTemp = '{0}&key={1}'.format(stringA, Mch_key)
    sign = hashlib.md5(stringSignTemp.encode("utf-8")).hexdigest()
    return sign.upper()

import time
import xmltodict
# 统一下单支付接口
def payOrder(request):
    #获取前端传过来的东东
    #allobj=request.POST.get("wxcartobj")#allobj None 直接取,取不到
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)

    params = parse_qs(body)
    # print(type(body))  # <class 'str'>
    data = json.loads(body)
    # print("data", data)
    # print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象-许",data['wxcartobj'])  #取到对象
    a = data['wxcartobj']#前端丢过来的所有数据,都在a里面


    myopenid=a['kkkopenid']#取到用户openid
    myuserinfo=a['kkkuser']#取到微信用户签名头像等详息
    mycartarray=a['kkkobj']#取到购物车对象数组
    myuserid=a['wxuserid']#取到操作的用户的id


    print("打印一下所有前端取到的4个数据myopenid",myopenid)
    print("打印一下所有前端取到的4个数据myuserinfo", myuserinfo)
    print("打印一下所有前端取到的4个数据mycartarray", mycartarray)
    print("打印一下所有前端取到的4个数据myuserid", myuserid)#经测试数据分离出来非常完美

    #计算要付的总金额,(可以从前端直接传过来的,但是没关系)
    totalprice=0
    for i in mycartarray:
        totalprice=totalprice+i["price"]*i["num"]
    print(totalprice)#OK,
    totalprice=totalprice*100#这一句在真实环境中要启用,这里单位是分,
                           #  前端要支付445,上面表示4.45元,金额小利用我测试,所以没有启用
    # 获取价格,和用户是谁
    price=totalprice#这一句真实环境要还原它,还原真实价格
    price=100#在这里,我为了方便测试,直接把金额写死成1元
    user_id=myuserid
    # 获取客户端ip   #下面这2句在真实环境中要还原它,把下面port和client的注释
    #print(request.get_host().split(":"))
    #client_ip, port = request.get_host().split(":")
    client_ip="127.0.0.1"
    port="80"
    # 获取小程序openid
    openid = myopenid

    # 微信官网的接口地址
    url = order_url

    # 拿到封装好的xml数据
    body_data = get_bodyData(openid, client_ip, price)
    print("跟踪订单编号-----------------------------", body_data)  # 经测试,里面正常代有订单编号,如下
    stestdic = xmltodict.parse(body_data, encoding='utf-8')
    mydindanbianhao2 = stestdic['xml']['out_trade_no']  # 取到了订单编号
    print("最终确认订单编号", mydindanbianhao2)
    # 获取时间戳
    timeStamp = str(int(time.time()))

    # 请求微信接口下单
    respone = requests.post(url, body_data.encode("utf-8"), headers={'Content-Type': 'application/xml'})

    # 回复数据为xml,将其转为字典
    content = xml_to_dict(respone.content)
    print("许飞content",content)
    # 返回给调用函数的数据
    #ret = {"state": 1000}
    if content["return_code"] == 'SUCCESS':
        # 获取预支付交易会话标识
        prepay_id = content.get("prepay_id")
        #prepay_id="我是许鹏飞"
        # 获取随机字符串
        nonceStr = content.get("nonce_str")

        # 获取paySign签名，这个需要我们根据拿到的prepay_id和nonceStr进行计算签名
        paySign = get_paysign(prepay_id, timeStamp, nonceStr)

        # 封装返回给前端的数据
        data = {"prepay_id": prepay_id, "nonceStr": nonceStr, "paySign": paySign, "timeStamp": timeStamp,"mydindanbianhao2":mydindanbianhao2}
        #data={"000":0}
        print('=========',data)

        #ret["msg"] = "成功"
        #return HttpResponse(data)
        return JsonResponse(data)

    else:
        return HttpResponse("失败")




























###################################################################################上面是支付

#########################################################################下面是支付后的数据入库

def gotodindan(request):
    # 获取前端传过来的东东
    # allobj=request.POST.get("wxcartobj")#allobj None 直接取,取不到
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)

    params = parse_qs(body)
    # print(type(body))  # <class 'str'>
    data = json.loads(body)
    # print("data", data)
    # print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象-许", data['wxcartobj'])  # 取到对象
    a = data['wxcartobj']#a 里面包括要写入数据库的所有数据

    myopenid = a['kkkopenid']  # 取到用户openid
    myuserinfo = a['kkkuser']  # 取到微信用户签名头像等详息
    mycartarray = a['kkkobj']  # 取到购物车对象数组
    myuserid = a['wxuserid']  # 取到操作的用户的id
    mydindannum = a['mydingdan']  # 取到订单编号

    print("打印一下所有前端取到的4个数据myopenid", myopenid)
    print("打印一下所有前端取到的4个数据myuserinfo", myuserinfo)
    print("打印一下所有前端取到的4个数据mycartarray", mycartarray)
    print("打印一下所有前端取到的4个数据myuserid", myuserid)  # 经测试数据分离出来非常完美
    print("打印一下所有前端取到的4个数据mydindannum", mydindannum)  # 经测试数据分离出来非常完美
    #上面经测试,已完美取到

    #取地址表默认地址
    e=ddaddress.objects.get(adefaultaddress=1)#经过地址问题的调整地址表中百分百有一条默认地址,支付时也一定有地址(mypay.vue做校验)
    myaddressid=e.id#获得地址ID
    print("取得默认地址的id",myaddressid)
    mykong=""
    fapiao=""
    fapiaohaoma=""
    paymode="1"
    payzt="SUCCESS"
    #totalprice在循环商品对象商组时写入中再计算

    #"wxdindan.wxuserid" must be a "myusertwo" instance   #myuserid
    objmyuser=myusertwommmm.objects.get(id=myuserid)#多表关联 ,写入订单表是,给的是一个myusertwo该id值的对象
    #"wxdindan.addressid" must be a "ddaddress" instance.
    #我们直接给地址表的默认地址对象

    #写入数据库,一款商款就写入一条订单,(一款是一个种类)
    for item in mycartarray:#循环出每一个商品对象
        mytotalprice=item['price']*item['num']
        myproid=item['id']
        mycount=item['num']
        wxdindan.objects.create(wxuserid=objmyuser,wxopenid=myopenid,wxusertext="",fapiao="",fapiaohaoma="",paymode="1",addressid=myaddressid,productid=myproid,count=mycount,payzt="SUCCESS",dindanbianhao=mydindannum,totalprice=mytotalprice)




    return HttpResponse("支付成功后所有数据写入订单表OK")





######################################################利用,用户id取所有订单
#######################################################################依用户id,取该用户所有订单的接口
class xiupro30kk(serializers.ModelSerializer):  # 序列化器订单表
    class Meta:
        model = wxdindan
        fields = "__all__"
        depth = 1
class xiupro31kk(serializers.ModelSerializer):  # 序列化器商品表
    class Meta:
        model = GProductmmmm
        fields = "__all__"
        depth = 1
class xiupro32kk(serializers.ModelSerializer):  # 序列化器地址表
    class Meta:
        model = ddaddress
        fields = "__all__"
        depth = 1




#主函数
def useralldindan(request):
    body_unicode = request.body.decode('utf-8')
    body = demjson.encode(body_unicode)
    body = json.loads(body)

    params = parse_qs(body)
    # print(type(body))  # <class 'str'>
    data = json.loads(body)
    # print("data", data)
    # print("data类型", type(data))  # dict字典,json对象
    print("接收前端的对象-许", data['uid'])  # 取到对象
    a = data['uid']#   a  就是前端传过来的用户 id



    # 取所有订单QuerySet对象
    e = wxdindan.objects.filter(wxuserid_id=a)
    print("e",e)#完美取到该用户的所有订单,对象数组...
    #但是还缺少商品详细数据,只有id,,,还有地址,也是一样


    #手动取商品对象QuerySet
    oproduct=[]
    for item in e:#循环每一条订单
        k=GProductmmmm.objects.get(id=item.productid)
        if k not in oproduct:#去重,已有,就别再加了
            oproduct.append(k)
    print("取出来的商品表对象数组",oproduct)
    print(333333333)

    #手动取出地址对象QuerySet
    oaddress = []
    for item in e:  # 循环每一条订单
        k = ddaddress.objects.get(id=item.addressid)
        if k not in oaddress:  # 去重,已有,就别再加了
            oaddress.append(k)
    print("取出来的商品表对象数组", oaddress)
    print(5555555555)



    serializer = xiupro30kk(e, many=True)
    # 把数据库数据调出来并序列化,成json传到前端
    ttt = {}
    jjj = serializer.data  # 取上面函数传出来的数据,是字典
    print(jjj)
    print("#" * 20)
    print(json.dumps(jjj))
    kdindan = json.dumps(jjj).encode('utf-8').decode('unicode_escape')  # 把数据字典转为JSON对象格式,前端才可以用

    serializer2 = xiupro31kk(oproduct, many=True)
    jjj2 = serializer2.data  # 取上面函数传出来的数据,是字典
    kproduct = json.dumps(jjj2).encode('utf-8').decode('unicode_escape')

    serializer3 = xiupro32kk(oaddress, many=True)
    jjj3 = serializer3.data  # 取上面函数传出来的数据,是字典
    kaddress = json.dumps(jjj3).encode('utf-8').decode('unicode_escape')



    ttt["kdindan"] = kdindan#kkk为订单序列对象数组
    ttt['kproduct']=kproduct#商品表
    ttt['kaddress'] = kaddress  # 商品表
    # return render(request,"course_shopcart.html",ttt)  ##这个是主函数,这个会往页面中增加数据
    #return HttpResponse(ttt)  # 这个会直接覆盖网页中所有的数据
    return JsonResponse(ttt)















































