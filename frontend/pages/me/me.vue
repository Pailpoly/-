<template>
	<view>
		<!-- 头 -->
		<view @click="bback" style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
		   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;">
			<text style="font-size: 30rpx;">关于我们</text>
		</view>
		<!-- 占高60rpx -->
		<view @click="bback" style="width:750rpx;height: 60rpx;background-color: #fff;"></view>
		
		<image @click="bback" style="width: 40rpx;height: 40rpx;margin-left: 20rpx;z-index: 20;"
		 src="/static/myimg/return.png"></image>
	<!-- 下面写内容吧 -->
	<view style="width: 750rpx;height: 100%;background-color: #fff;margin-top: 100rpx;
	     box-sizing: border-box;padding: 0 10rpx 10rpx 20rpx;">
		 <view class="myview">
			 <text>官网:https://www.duanshuiLu.com/</text>
		 </view>
		 <view class="myview">
		 			 <text>微信:15323441764</text>
					 
		 </view>
		 <view class="myview">
		 			 <text>QQ:2502045294</text>
		 </view>
		 
	</view>
	
	<view class="myview">
		<text>
			可以上本公司的官网,免费看视频
		</text>
	</view>
	<view class="myview">
		<text>
			可以加本人微信,索取开发文档
		</text>
	</view>
	<view class="myview">
		<text>
			可以加本人QQ,学习过程中的难点,都可以问我
		</text>
	</view>
	<!-- 上面写内容吧 -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			///返回
			bback(){
				uni.switchTab({
					url:"../personal/personal"
				})

			}
			///
		}
	}
</script>

<style>
.myview{
	margin-top: 100rpx;
	font-size: 40rpx;
	color: #c32136;
}
</style>