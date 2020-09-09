<template>
	<view>
<!-- 标题  -->		
		<!-- 头 -->
		<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
		   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;">
			<text style="font-size: 30rpx;">{{myusername}}-欢迎光临东京商城</text>
		</view>	
<!-- 搜索框  -->
<view style="height: 250rpx;width: 750rpx;"></view>
  <!-- 搜索框  -->
  
<view style="position: fixed;top: 140rpx;left: 0;width: 750rpx;height: 60rpx;z-index: 200;">
<view class="search-block" >
	
	<view  style="width: 40rpx;height: 60rpx;background-color:#FFFFFF;position: fixed;
	top: 110rpx;left: 130rpx;">
		
	</view>
	
 <view class="search-ico-wapper">
	  <image style="margin-top: 3rpx;margin-left: 6rpx;z-index: 80;" src="../../static/myimg/chongzhi-icon-sousuo@3x.png" class="search-ico" mode=""></image>
  </view>
  <input style="margin-left: 10rpx;" type="text" value="" placeholder="输入关键词进行搜索" class="search-text" maxlength="10" />
 <view class="search-ico-wapper1">
	  <image style=""
	   src="../../static/myimg/chongzhi-icon-sys@3x.png" class="search-ico-1" mode=""></image>
  </view>
</view>
<view class="shadow">

</view>	
	</view>
  <!-- 上面是搜索框  --> 
	
<!-- 上面是搜索框  -->			
			
			
<view style="position: fixed;">
	<good></good>
</view><!-- 使用good组件 -->
			
			
			
			
			
			
			
			
	</view>
</template>

<script>
	import good from "../../comm/good.vue"
	export default {
		data(){
			return{
				islogin:false,//掌控用户是否登陆机制,没有登陆为false
				myusername:""//取用户名
			}
	
		},
		components:{
			good
		},
		onLoad() {
			let a=uni.getStorageSync("myopenid")
			//console.log("a",a)
			if(a==""){
				//没有登陆过
				uni.navigateTo({
				                url: '/pages/wxlogin/wxlogin',
				            });
			}else{
				this.islogin=true
				console.log(this.islogin)
			}
			
		},
		onShow() {
			let a=uni.getStorageSync("myopenid")
			//console.log("a",a)
			if(a==""){
				this.islogin=false
				//没有登陆过
				uni.navigateTo({
				                url: '/pages/wxlogin/wxlogin',
				            });
			}else{
				this.islogin=true
				console.log(this.islogin)
			}
			let yname=uni.getStorageSync("myuser").nickName
			this.myusername=yname
			
		}
	}
</script>

<style scoped>
/* <!-- 下面是搜索框  --> */


page{
    background-color: #FFFFFF;
}

.search-ico, .search-ico-1{
    width: 35upx;
    height: 35upx;
}
.search-text{
    font-size: 14px;
    background-color: #FFFFFF;
    height: 60upx;
    width: 480upx;
}
.search-block{
    display: flex;
    flex-direction: row;
    padding-left: 60upx;
    position: relative;
    top: -32upx;
}
.search-ico-wapper{
    background-color: #FFFFFF;
    display: flex;
    flex-direction:column;
    justify-content: center;
    padding: 0upx 0upx 0upx 40upx;
    border-bottom-left-radius:18px;
    border-top-left-radius: 18px;
}
.search-ico-wapper1{
    background-color: #FFFFFF;
    display: flex;
    flex-direction:column;
    justify-content: center;
    padding: 0upx 40upx 0upx 0upx;
    border-bottom-right-radius:18px;
    border-top-right-radius: 18px;
}
.shadow{
    width: 638upx;
    height: 60upx;
    border-radius:18px;
    -moz-box-shadow:0 0 10px #e6e6e6;
    -webkit-box-shadow:0 0 10px #e6e6e6;
    box-shadow:0 0 10px #e6e6e6;
    position: relative;
    top: -90upx;
    left: 60upx;
}
/* 上面是搜索框CSS */
</style>