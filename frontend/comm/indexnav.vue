<template>
  <view class="content">
	
	  <view class="header">
		    <view class="left">
				<!--  -->
				<image src="/static/myimg/shu.png" mode=""></image>
				<view class="location-box">
						<view class="city">
							深圳市
						</view>
						<view style="margin-top: 8rpx;" class="location">
							深圳华强北88号
						</view>
				</view>
				
				
			</view>
			
			<view class="right">
				
			</view>
	  </view>
	  
	  <view class="box">
		  
	  </view>
	  
  </view>
</template>

<script>
	export default {
		
	}
</script>

<style scoped>
.content{
	background-color: white;
	
}
.header{
	height: 80rpx;padding-top: 50rpx;
}
.left{
	float: left;overflow: hidden;
	
}
.left image{
	height: 70rpx;width: 70rpx;border-radius: 35px;
	float: left;margin: 0 30rpx;
}
.city{
	height: 35rpx;line-height: 35rpx;font-size: 35rpx;
}
.location-box{
	float: left;height: 70rpx;
}
.location{
	height: 35rpx;line-height: 35rpx;font-size: 20rpx;
}
</style>