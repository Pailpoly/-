<template>
	<view>
<view style="width: 750rpx;height: 200rpx;margin-top: 15rpx;">
	<!-- 左侧的第一个div -->
	<view style="font-weight: bold;width: 180rpx;text-align: center;">
		<view style="position: relative;top: 30rpx;"><text>我的积分</text></view>
		<view style="position: relative;top: 40rpx;"><text>8888</text></view>
	</view>
	
	<!-- 右侧大的div -->
	<view style="font-size: 26rpx;display: flex;
	           justify-content: space-between;width: 550rpx;position: relative;left: 180rpx;
			   top: -50rpx;">
		<!-- 第一个块 -->
		<view>
			<view>
				<image style="width: 80rpx;height: 80rpx;" src="/static/myimg/ma.png"></image>
			</view>
			<view>
				<view style="width: 10rpx;height: 8rpx;"></view>
				<text>会员码</text>
			</view>
		</view>
		<!--  -->
		<view>
			<view>
				<image style="width: 80rpx;height: 80rpx;" src="/static/myimg/ka.png"></image>
			</view>
			<view>
				<view style="width: 10rpx;height: 8rpx;"></view>
				<text style="display;width: 12rpx;height: 6rpx;display: inline-block;"></text>
				<text>卡包</text>
			</view>
		</view>
		<!--  -->
		<view>
			<view>
				<image style="width: 80rpx;height: 80rpx;" src="/static/myimg/quan.png"></image>
			</view>
			<view>
				<view style="width: 10rpx;height: 8rpx;"></view>
				<text>优惠券</text>
			</view>
		</view>
		<!--  -->
		<view>
			<view>
				<image style="width: 80rpx;height: 80rpx;" src="/static/myimg/qianbao(1).png"></image>
			</view>
			<view>
				<view style="width: 10rpx;height: 8rpx;"></view>
				<text style="display;width: 15rpx;height: 6rpx;display: inline-block;"></text>
				<text>钱包</text>
			</view>
		</view>
		
		
	</view>
</view>
<!-- <view style="padding: ;box-sizing: border-box;"></view> -->

<!-- 水平线 -->
<view style="width: 750rpx;height: 2rpx;background-color: #e9e7ef;margin-top: -20rpx;">
	
</view>
	</view>
</template>

<script>
	export default {
		
	}
</script>

<style scoped>
.text1{
	margin-top: 6rpx;
}
</style>