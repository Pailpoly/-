<template>
	<view>
		
		
<!-- 头 -->
<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
   position:fixed;color:#fff;z-index: 10;top: 50rpx;font-weight: bolder;">
	<text style="font-size: 30rpx;">您的订单</text>
</view>
<!-- 头的提示 -->
<view style="width: 750rpx;height: 200rpx;background-color: #ff4e20;color: #fff;font-size: 26rpx;
         display: flex;justify-content: center;align-items: center;">
	<view style="position: relative;top: 50rpx;left: 0rpx;">顺丰速运/邮政</view>
	<view style="width: 20rpx;hei20rpx"></view>
	<view style="position: relative;top: 50rpx;left: 0rpx;">|</view>
	<view style="width: 20rpx;hei20rpx"></view>
	<view style="position: relative;top: 50rpx;left: 0rpx;">正常3日达</view>
</view>
<!-- 返回按钮箭头 -->
<view>
	<image  @click="tiaomypay"  
	style="position: fixed;top: 50rpx;left: 15rpx;width: 40rpx;height: 40rpx;z-index: 88;" 
	src="../../static/myimg/rightmm.png">
		
	</image>
</view>
<!-- 下面是显示订单 -->
<!-- 下面是显示订单 -->
<!-- 下面是显示订单 -->
<!-- 下面是显示订单 -->
<view><!-- 外框,好固定单一订单显示的高宽 -->
	<view v-for="item in mydingdanarray" style="color: #000000;z-index: 888;font-size: 26rpx;
	            margin-bottom: 30rpx;line-height: 30rpx;margin-left: 12rpx;">
		 <view>
			 <text>{{item.add_time | formatDate}}</text>
			 <text></text>
		 </view>
		 <view style="margin-top: 10rpx;">
			 <text>订单编号:{{item.dindanbianhao}}</text>
		 </view>
		 <view style="margin-top: 60rpx;position: absolute;right: 20rpx;">
			 <text>数量{{item.count}}</text>
		 </view>
		 <view style="margin-top: 95rpx;position: absolute;right: 20rpx;">
			 <text>付款{{item.totalprice}}</text>
		 </view>
		 <view style="margin-top: 15rpx;color: #dc3023;font-weight: bold;right: 20rpx;">
			 <text>{{item.productinfo.name}} </text>
		 </view>
		 <view style="margin-top: 10rpx;">
<image style="width: 130rpx;height: 130rpx;"
	:src="'/static/'+item.productinfo.small_image">
</image>
		 </view>
		 <view style="margin-top: -20rpx;position: absolute;right: 10rpx;">
		 			 		<view style="width: 200rpx;height: 50rpx;border-color: #dc3023;border-radius: 25rpx;
		 			 					display: flex;justify-content: center;align-items: center;
		 			 		         border-width: 2rpx;border-style: solid;margin-left: 125rpx;z-index: 880;">
		 			 			<text style="color: #dc3023;font-size: 26rpx;">查看订单详情</text>
		 			 		</view>
		 </view>
		 <!-- 地址 -->
		 <view style="margin-top: 10rpx;color: #808080;">
		 			 <view>
		 				 <text>{{item.addressinfo.aname}}</text>
						 <text style="width: 10rpx;height: 10rpx;margin-left: 10rpx;"></text>
						 <text>{{item.addressinfo.aphone}}</text>
		 			 </view>
		 </view>
		 <view style="margin-top: 10rpx;color: #808080;">
		 			 <view>
		 				 <text>{{item.addressinfo.city}}</text>
						 <text>{{item.addressinfo.aaddress}}</text>
		 			 </view>
		 </view>
		 <!-- 上面是地址 -->
		 
		 <view style="width: 750rpx;border-bottom-style: solid;border-bottom-width: 2rpx;
		     border-bottom-color: #e9e7ef;margin-top: 10rpx;">
			 
		 </view>

		 
	</view>
</view>
<!-- 显示订单结束 -->
</view>
<!--  -->
<!--  -->
<!--  -->



<!-- 显示订单结束 -->






















			
	</view>
</template>

<script>
	export default {
		data() {
			return {
				mydingdanarray:[],//存订单
				myproductarray:[],//存商品
				myaddressarray:[]//存地址
			}
		},
onLoad() {//////
		var tthat=this
			//提取用户id
			let uid=uni.getStorageSync("userid")
			console.log("提取到用户id为",uid)//测试正常,取到
			/////
			uni.request({
				url: 'http://127.0.0.1/useralldindan/', //。
				data: {
					uid: uid
				},
				method: 'POST',
				header: {
					// 'custom-header': 'hello' //自定义请求头信息
				},
				success: res => {
					console.log(res);
								// 先不存本地.3个对象要完全容合
								let dingdanarray=res.data.kdindan
								let productarray=res.data.kproduct
								let addressarray=res.data.kaddress
								console.log(dingdanarray)
								console.log(productarray)
								console.log(addressarray)
								tthat.mydingdanarray=JSON.parse(dingdanarray)
								tthat.myproductarray=JSON.parse(productarray)
								tthat.myaddressarray=JSON.parse(addressarray)
								console.log("this.mydingdanarray",tthat.mydingdanarray[0])//取到第一个订单
///////////////
			//容合三个对象数组
			tthat.mydingdanarray.forEach(function(item){//遍历每一个订单
				//item.addressid
					tthat.myaddressarray.forEach(function(m){
						//m.id
							if(m.id==item.addressid){
								item["addressinfo"]=m//地址相对,把整个地址添加订单对象
							}
						})
			})
			console.log("看订单和地址容合没",tthat.mydingdanarray[0])//完美容合地址和订单
			
			//容合三个对象数组2
			tthat.mydingdanarray.forEach(function(item){//遍历每一个订单
				//item.productid
					tthat.myproductarray.forEach(function(m){
						//m.id
							if(m.id==item.productid){
								item["productinfo"]=m//地址相对,把整个地址添加订单对象
							}
						})
			})
			console.log("看订单和地址容合没",tthat.mydingdanarray[0])//3个完美容合
//////////////
		
				},
				fail: res => {}
			});
			/////
			
			
},//////////////
		
		
methods: {///
	tiaomypay(){
		console.log("跳转函数运行了")
		uni.switchTab({
			url: '/pages/personal/personal'
		})
		uni.navigateTo({
			url: '/pages/personal/personal'
		})
	}///
},///
// 时间过滤器
filters: {
            formatDate: function(value) {
                var date = new Date();
                //date.setTime(value);
                var month = date.getMonth() + 1;
                var hours = date.getHours();
                if (hours < 10)
                    hours = "0" + hours;
                var minutes = date.getMinutes();
                if (minutes < 10)
                    minutes = "0" + minutes;
                var time = date.getFullYear() + "-" + month + "-" + date.getDate() +
                    " " + hours + ":" + minutes;
                return time;
            }
 
        },
//////
	}
</script>

<style>

</style>
