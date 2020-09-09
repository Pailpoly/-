<template><!-- 如果没有登陆 -->
	<view>
<!-- 会员信息页标题  -->
		<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
		   position:fixed;color:#f00056;z-index: 10;top: 50rpx;font-weight: bolder;">
			<text style="font-size: 30rpx;">会员中心</text>
		</view>
		<view class="member-top">
<!-- 如果用户微信没有设头象 -->
<template v-if="!myuserinfo"><!-- 如果没有登陆 -->
	<image src="../../static/myimg/empty-tx.png" class="member-tx" mode=""></image>
</template>
<template v-else>
<!-- 如果登陆,则显示用户微信头像 -->
<image :src="myuserinfo.avatarUrl" class="member-tx" mode=""></image>
</template>
			
			
			<view class="userinfo">
<!-- 如果用户没有登陆 -->
<!-- 如果用户没有登陆 -->
				<view class="loginReg" v-if="!myuserinfo">
					<navigator url="../login/login" hover-class="none">登陆/注册</navigator>
				</view>
<!-- 如果用户有登陆 -->
				<view class="loginInfo" v-else>
					<template v-if="myuserinfo.nickName">
						<text class="username">{{myuserinfo.nickName}}</text>
					</template>
					<template v-else>
						<text class="username">duanshuiLu.com</text>
					</template>
					
					<text class="nickname">{{myuserinfo.city}}</text>
				</view>
			</view>
<!-- 二维码图片 -->
			<view class="ewm">
				<image src="../../static/myimg/ewm.png" mode=""></image>
			</view>
			<!-- #ifndef MP-WEIXIN -->
			<view class="memberIcon">
				<i class="iconfont">&#xe612;</i>
				<i class="iconfont" @click="href('./setting')">&#xe614;</i>
			</view>
			<!-- #endif -->
			
		</view>
		<view class="orderStatus">
			<view class="orderItem" @click="statusHref(1)">
				<image src="../../static/myimg/member-icon1.png" mode=""></image>
				<text>待付款</text>
			</view>
			<view class="orderItem" @click="statusHref(2)">
				<image src="../../static/myimg/member-icon2.png" mode=""></image>
				<text>待发货</text>
			</view>
			<view class="orderItem" @click="statusHref(4)">
				<image src="../../static/myimg/member-icon3.png" mode=""></image>
				<text>待评价</text>
			</view>
			<view class="orderItem" @click="statusHref(0)">
				<image src="../../static/myimg/member-icon4.png" mode=""></image>
				<text>全部订单</text>
			</view>
		</view>
		<view class="spliteLine"></view>
		<view class="menuList">
			<view class="menuItem" @click="href('../address/list')">
				<!-- <navigator url="../address/list" hover-class="none"> -->
				<image src="../../static/myimg/member-menu1.png" mode=""></image>
				<text>收获地址</text>
				<!-- </navigator> -->
			</view>
			<view class="menuItem" @click="kefu">
				<image src="../../static/myimg/member-menu2.png" mode=""></image>
				<text>在线客服</text>
			</view>
			<!-- <a href="mqqwpa://im/chat?chat_type=wpa&uin=381232999&version=1&src_type=web&web_src=oicqzone.com">11231</a> -->
			<view class="menuItem">
				<image src="../../static/myimg/member-menu3.png" mode=""></image>
				<text>邀请有礼</text>
			</view>
			<view class="menuItem" @click="me">
				<image src="../../static/myimg/member-menu4.png" mode=""></image>
				<text>关于我们</text>
			</view>
			<view class="menuItem"  @click="href('/pages/member/setting')">
				<image src="../../static/myimg/member-menu4.png" mode=""></image>
				<text>设置</text>
			</view>
		</view>
		<!--  -->
<view style="background-color: #f0f0f4;color: #c32136;" class="logout" @click="logout" v-if="myuserinfo">
	退出登录
</view>
	</view>
</template>

<script>
	import {mapState} from "vuex"
	export default {
		data() {
			return {
				myuserinfo:{},//从本地判断用户登陆否
				code:'',
				member:[],
				imgUrl:this.$imgUrl
			};
		},
		computed:{
			//...mapState(["isLogin","userinfo"])
		},
		onLoad() {
			let p=uni.getStorageSync('myuser')//用同步,取出数组
						//判断对象是否为{} 空
						let k=Object.keys(p)
						if(k.length==0){
							this.myuserinfo={}
						}else{
							this.myuserinfo=p
						}
						console.log("个人信息页的onload,this.myuserinfo",this.myuserinfo)
		},
		onShow() {
			this.getData()
		},
		
		methods:{
			///关于我们
						me(){
							uni.navigateTo({
								url:"/pages/me/me",
								success:res =>{},
								fail:() =>{},
								complete:() => {}
							})
			
							               
						},
						///
			kefu(){
				// var url="mqq://im/chat?chat_type=wpa&uin=88888888&version=1&src_type=web"
				// plus.runtime.openURL(url,function(res){
				// 	plus.nativeUI.confirm("检查到您未安装QQ", function(i) {  
				// 		 if (i.index == 0) {  
				// 				  plus.runtime.openURL("http://www.baidu.com")
				// 		 }  
				// 	});  
					
				// })
			},
			
			
			
			statusHref(index){
				//this.$href('/pages/member/orderlist?status='+index)
			},
			href(url){
				//this.$href(url)
			},
			logout(){
				///退出登陆
						
				uni.removeStorageSync('myopenid');//同步删除
				uni.removeStorageSync('myuser');
				uni.showToast({
					title: '注销登陆',
					duration: 1000
				});
				uni.switchTab({
									url:"/pages/index/index",
									success:res =>{},
									fail:() =>{},
									complete:() => {}
								});
						
			},
			getData(){
				// this.$request('/member/index')
				// .then(res=>{
				// 	console.log(res)
					
				// 	// res.data.image=this.$imgUrl+res.data.image
				// 	// this.code=res.code;
					
				// 	if(res.code==1){
				// 		this.$store.commit('login',res.data)
				// 		this.member=res.data;
				// 	}
				// })
			},
			statusHref(index){
							if(index==0){
								uni.switchTab({
									url: '/pages/seeorder/seeorder'
								})
								uni.navigateTo({
									url: '/pages/seeorder/seeorder'
								})
							}
						},
			
		}
	}
</script>

<style>
.member-top{height: 336rpx;background: url(../../static/myimg/member-top.png) no-repeat;
background-size: 100% 336rpx;position: relative;}
.member-tx{width: 110rpx;height: 110rpx;position: absolute;top:165rpx;left:30rpx;
border-radius: 50%;}
.loginReg{width: 160rpx;height: 45rpx;color: #fff;border:1rpx solid #fff;font-size: 28rpx;
text-align: center;line-height: 45rpx;position: absolute;top:190rpx;left:160rpx;}
.loginInfo{position: absolute;top:180rpx;left:160rpx;}
.loginInfo text.username{line-height: 42rpx;height: 42rpx;font-size: 28rpx;color: #fff;display: block;}
.loginInfo text.nickname{line-height: 38rpx;height: 38rpx;font-size: 24rpx;color: #fff;display: block;}
.ewm{height: 35rpx;width: 35rpx;position: absolute;top:200rpx;right:30rpx;}
.ewm image{width: 35rpx;height: 35rpx;}
.memberIcon{position: absolute;top:50rpx;right: 30rpx;color: #fff;}
.memberIcon i{margin-left: 35rpx;}

.orderStatus{display: flex;}
.orderItem{width:25%;}
.orderItem image{width: 70rpx;height: 56rpx;display: block;margin:20rpx auto 0;}
.orderItem text{display: block;line-height: 80rpx;font-size: 28rpx;text-align: center;padding-bottom: 10rpx;}
.spliteLine{height: 20rpx;width: 100%;background: #f5f5f5;}

.menuItem {height: 90rpx;margin:0 30rpx;border-top: 1rpx solid #e5e5e5;
font-size:28rpx ;display: flex;align-items: center;
background: url(../../static/myimg/more.png)  no-repeat ;
background-size: 26rpx 26rpx;
background-position: right center;
}
.menuItem:nth-of-type(1){border-top:none;}
.menuItem image{width: 30rpx;height: 30rpx;margin-right: 25rpx;}
.logout{margin:30rpx;height: 85rpx;border:1rpx solid #e5e5e5;font-size: 28rpx;text-align: center;
line-height: 85rpx;}
</style>